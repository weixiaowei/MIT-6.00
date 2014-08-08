def payoff_in_year(balance,annualInterestRate):

    monthly_Rate = annualInterestRate / 12.0
    remaining_Balance = balance
    low = balance / 12
    upper = (balance * (1+monthly_Rate)**12) / 12.0
    lowest_Paid = round((low+upper) / 2.0, 2)
    epsilon = - 0.5
    
    while remaining_Balance < epsilon or remaining_Balance > 0:

        #I make a mistake in here,remaining_Balance should be initialize each loop
        remaining_Balance = balance
        #print remaining_Balance

        month = 1
        while month < 13:
            remaining_Balance = round((remaining_Balance - lowest_Paid) * (1 + monthly_Rate),2)
            month += 1
        print remaining_Balance
            
        if remaining_Balance > 0:
            low = lowest_Paid
        elif remaining_Balance < epsilon:
            upper = lowest_Paid
        else:
            break
        lowest_Paid = round((low+upper) / 2.0, 2)

    print 'Lowest paid is: ', lowest_Paid, remaining_Balance
