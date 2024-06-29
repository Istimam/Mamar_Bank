from django.urls import path
from .views import DepositMoneyView, WithdrawMoneyView, TransactionReportView, LoanRequestView, PayLoanView, LoanListView

urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loan_request/", LoanRequestView.as_view(), name="loan_request"),
    path("loan/<int:pk>/", PayLoanView.as_view(), name="loan_pay"),
]
