from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type']

    # disabling transaction_type
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance 
        return super().save()

class DepositeForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korlm
        min_deposite_amount = 100
        amount = self.cleaned_data.get('amount') #user er fill up kota form theke amra amount field er balire ke niye ashlm
        if amount < min_deposite_amount:
            raise forms.ValidationError(f'Minimum deposit amount is {min_deposite_amount}$')
        return amount
    
class WithdrawForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korlm
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance #1000
        amount = self.cleaned_data.get('amount') #user er fill up kota form theke amra amount field er balire ke niye ashlm
        if amount < min_withdraw_amount:
            raise forms.ValidationError(f'Minimum withdraw amount is {min_withdraw_amount}$')
        elif amount > max_withdraw_amount:
            raise forms.ValidationError(f'Maximum withdraw amount is {max_withdraw_amount}$')
        elif amount > balance: # amount = 5000, balance = 2000
            raise forms.ValidationError('Insufficient balance')
        return amount
    
class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount
