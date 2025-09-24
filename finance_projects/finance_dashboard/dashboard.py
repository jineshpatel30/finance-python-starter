# Finance Tools Dashboard
# Lets user choose between 5 mini-projects

import future_value
import savings_simulation
import loan_repayment_schedule
import portfolio_tracker
import currency_converter

def menu():
    print("\n=== Finance Tools Dashboard ===")
    print("1. Future Value Calculator")
    print("2. Savings Simulation")
    print("3. Loan Repayment Schedule")
    print("4. Portfolio Tracker")
    print("5. Currency Converter")
    print("0. Exit")

while True:
    menu()
    choice = input("Choose a tool (0-5): ")

    if choice == "1":
        future_value.run()
    elif choice == "2":
        savings_simulation.run()
    elif choice == "3":
        loan_repayment_schedule.run()
    elif choice == "4":
        portfolio_tracker.run()
    elif choice == "5":
        currency_converter.run()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
