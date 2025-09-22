name = input("what is your name? ")

match name:
    #case "Harry":
    #    print("Gryffiendor")
    #case "Hermione":
    #    print("Gryffiendor")
    case "Harry" | "Hermione" | "Ron":  #for match function | works as "or", we can't use and/or directly
        print("Gryffiendor")
    case "Draco":
        print("Slytherin")
    case _: #catch all for match is _
        print("Who?")

#
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffiendor")
elif name == "Draco":
    print("Syltherian")
else:
    print("Who?")
