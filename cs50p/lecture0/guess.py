def get_guess():
    guess = int(input("guess a number : "))
    return guess

def main():
    guess = get_guess()    #we can use same variable number under differnt functions, it will be limited to that perticular function
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect, take another guess")

main()
