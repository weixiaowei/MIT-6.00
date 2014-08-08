def Paying_minimum(balance,annual_Interest_Rate,monthly_Payment_Rate):
    month = 1
    remaining_Balance = balance
    monthly_Interest_Rate = annual_Interest_Rate / 12
    total_Paid = 0
    
    while month < 13:

        minimum_Monthly_Payment = round(remaining_Balance * monthly_Payment_Rate, 2)
        remaining_Balance = round((remaining_Balance - minimum_Monthly_Payment) * (1 + monthly_Interest_Rate), 2)

        print 'Month: ', month
        print 'Minimum monthly payment: ', minimum_Monthly_Payment
        print 'Remaining balance: ', remaining_Balance
        
        total_Paid += minimum_Monthly_Payment
        month += 1

    print 'Total paid: ', total_Paid
    print 'Remaining balance: ', remaining_Balance
