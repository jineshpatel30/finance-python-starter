emoticon = "v-v"  #global variable, can only be modified by function by specifically defining inside the function

def main():
    global emoticon
    say("Knock knock.")
    emoticon = ":D"  #stays grey till you specify global variable in function to allow in-function modification
    say("Hey there!")


def say(phrase):
    print(phrase , emoticon)


main()
