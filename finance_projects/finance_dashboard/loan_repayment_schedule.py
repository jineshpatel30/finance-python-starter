# Loan Repayment Calculator
def run():
    loan = int(input("What is loan amount? "))
    payment = int(input("Monthly EMI: "))
    annual_rate = float(input("Annual Intrest Rate (in %): "))
    total_interest = 0
    rate = annual_rate/(100*12)

    month = 1
    while loan > 0:
        interest = loan * rate
        total_interest += interest
        principal_payment = payment - interest
        loan -= principal_payment
        if loan < 0:
            loan = 0
        print(f"Month {month}: Interest={round(interest, 2)}, "
            f"Principal={round(principal_payment, 2)}, Remaining={round(loan, 2)}, "
            f"Total Interest Paid = {round(total_interest, 2)}")
        month += 1