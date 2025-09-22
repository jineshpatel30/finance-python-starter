while True:  # while statement is similar to if (executed only once), but executed mutiple times till Condition is met/Ture.
    number = int(input("Provide a number, 0 stops: "))
    if number == 0:
        break
    elif number != 0:  #not required, using as an example for "pass" which is used for by-passing a condition while doing code itterations.
        pass
    print(f"Number times 10 = {number*10}")

