def creditcard_balance(balance,annualInterestRate,monthlyPaymentRate):
    """
    Input:balance - the outstanding balance on the credit card
          annualInterestRate - annual interest rate as a decimal
          monthlyPaymentRate - minimum monthly payment rate as a decimal
    Return:the remain balance after a year
    """
    monthlyInterestRate = annualInterestRate/12.0
    for i in range(12):
        minimumMonthlyPayment = monthlyPaymentRate*balance
        balance -= minimumMonthlyPayment
        balance += balance*monthlyInterestRate
        print('Month %d remaining balance:%.2f'%(i+1,balance))
    return round(balance,2)

creditcard_balance(484,0.2,0.04)
