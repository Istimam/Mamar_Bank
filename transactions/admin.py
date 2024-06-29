from django.contrib import admin
from .models import Transaction
from .views import send_transaction_mail
# Register your models here.
# admin.site.register(Transaction)
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'timestamp', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve')

    def save_model(self, request, obj, form, change):
        if obj.loan_approve == True:
            obj.account.balance += obj.amount
            obj.balance_after_transaction = obj.account.balance
            obj.account.save()
            send_transaction_mail(obj.account.user, obj.amount, "Loan Approve", "transactions/loan_approve_message.html")
        super().save_model(request, obj, form, change)