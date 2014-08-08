def payoff_in_year(balance,annualInterestRate):

    monthly_Rate = annualInterestRate / 12.0
    

    for lowest_Paid in range(10,balance,10):

        #I make a mistake in here,remaining_Balance should be initialize each loop
        remaining_Balance = balance


        month = 1
        while month < 13:
            remaining_Balance = round((remaining_Balance - lowest_Paid) * (1 + monthly_Rate),2)
            #print remaining_Balance
            month += 1
        
        if remaining_Balance <= 0:
            break
        
        
    print 'Lowest paid is: ', lowest_Paid, remaining_Balance
    
    
    
    
def payoff_in_year(balance,annualInterestRate):

    monthly_Rate = annualInterestRate / 12.0
    remaining_Balance = balance
    lowest_Paid = 0
    

    while remaining_Balance > 0:

        #I make a mistake in here,remaining_Balance should be initialize each loop
        remaining_Balance = balance


        month = 1
        while month < 13:
            remaining_Balance = round((remaining_Balance - lowest_Paid) * (1 + monthly_Rate),2)
            #print remaining_Balance
            month += 1


        if remaining_Balance > 0:
            lowest_Paid += 10
        
    print 'Lowest paid is: ', lowest_Paid, remaining_Balance

