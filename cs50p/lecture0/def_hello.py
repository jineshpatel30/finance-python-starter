def hello(to="world"):
    print("hello, ", to, ". Welcome!", sep="")

hello(input("What's your name? "))

'''
Funcation needs to be defined before it is "called"
By defining the main progam in seperate "main" fuction from others, preferably at top, though
irrespective of the order, we can call main at the end and since all functions will come before,
It will make them callable by each other if inter-linked properly and in main

def hello(to="world"):
    print("hello,", to)
'''
