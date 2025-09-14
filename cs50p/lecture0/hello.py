name = input ("What is your name? ")

#name = name.capitalize()
name = name.strip().title()
#name = input ("What is your name? ").strip().title()

first, last = name.split()

#print(*objects, sep=' ', end='\n', file=None, flush=False)
#print("hello, ")
#print(name)
#print("hello, ", end="")
#print(name)
#print("hello, " + name)
#print("hello, ", name)
#print("hello, ", name, sep="") #Seperator changes behaviour of auto space between two arguments

print(f"hello, {first}")
