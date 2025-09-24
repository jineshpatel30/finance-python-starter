# Savings Simulation with monthly deposits + interest
def run():
    deposit = int(input("Monthly deposit amount: "))
    balance = int(input("Current account balance: "))
    months = int(input("Investment horizon in months: "))
    annual_rate = float(input("Annaul intrest rate (in %)? "))

    rate = annual_rate/(100*12)

    for m in range(1, months + 1):
        balance += deposit
        balance *= (1 + rate)
        print(f"Month {m}: Balance = {round(balance, 2)}")

    print(f"Final balance after {months} months: {round(balance, 2)}")
