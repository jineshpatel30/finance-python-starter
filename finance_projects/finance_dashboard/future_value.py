# Future Value Calculator
# Formula: FV = PV * (1 + r)^t
def run():
    principal = int(input("Provide an investment amount: "))
    rate = float(input("What is an annaul intrest rate (in %)? "))
    freq = input("Compounding - Annual/Semi-Annual/Quarterly/Monthly/Daily? ").strip().lower()
    years = int(input("Provide an investment period in years: "))

    rate /= 100

    if freq == "daily":
        freq = 365
    elif freq == "monthly":
        freq = 12
    elif freq == "quarterly":
        freq = 4
    elif freq == "Semi-Annual":
        freq = 2    
    else:
        freq = 1

    value = principal
    for year in range(years):
        value *= (1 + (rate/freq))**freq

    print(f"Future Value after {years} years: {round(value, 2)}")
