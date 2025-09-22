def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    return n % 2 == 0 #returns bools directly so no need to specify with if conditions
    #return True if n % 2 == 0 else False
    '''
    if n % 2 == 0:
        return True #T/F capital
    else:
        return False
    '''

main()

