def greet(input):
    if "hello" in input:
        #print("hello, there!") #side effect, cannot be used further in the code, while return can be used
        return "hello, there!"
    else:
        #print("Hm, I'm not sure what you mean.")
        return "Hm, I'm not sure what you mean."

greeting = greet(input("Say hello to start: ").lower())
print(greeting + " I'm a greeting bot")
