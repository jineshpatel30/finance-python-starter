# Currency Converter (USD <-> EUR)
def run():
    def convert(amount, rate, direction="USD_to_EUR"):
        if direction == "USD_to_EUR":
            return amount * rate
        elif direction == "EUR_to_USD":
            return amount / rate
        else:
            return None

    input_currency = input("Which currency would you like to convert - USD/EUR: ").strip().upper()
    if input_currency == "USD":
        convert_currency = "EUR"
        direction = "USD_to_EUR"
    elif input_currency == "EUR":
        convert_currency = "USD"
        direction = "EUR_to_USD"
    else:
        print("Enter a valid input currency")
        quit()  #https://www.codecademy.com/article/python-exit-commands-quit-exit-sys-exit-os-exit-and-keyboard-shortcuts
        
    input_amount = float(input(f"What is {input_currency} amount: "))
    convert_amount = convert(input_amount, 0.85, direction) #USDEUR as of 24 Sep 2025
    print(f"{input_amount} {input_currency} = {round(convert_amount, 2)} {convert_currency}"
        f"\n<Note: USD-EUR conversion rate used as of 24 Sep 2025>")