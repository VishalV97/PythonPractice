balance = 320000
initial_balance = balance
annualInterestRate = 0.2
high = (initial_balance*(1 + annualInterestRate/12.0)**12)/12.0
lo = initial_balance/12.0
alpha = 0.01

while abs(balance) > alpha:
    monthlyPayment = (lo + high)/2
    balance = initial_balance
    for i in range(12):
        balance = balance - monthlyPayment + ((balance - monthlyPayment)*annualInterestRate/12.0)
    if balance > alpha:
        lo = monthlyPayment
    elif balance < -alpha:
        high = monthlyPayment
    else:
        break

print("Lowest Payment:", round(monthlyPayment, 2))
