def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Mutiplayer or Single? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Pocker")
        elif players == "Single":
            recommend("Klondike")
        else:
            print("Enter a valid input for players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single":
            recommend("Clock")
        else:
            print("Enter a valid input for players")
    else:
        print("Enter a valid input for difficulty")

def recommend(game):
    print("you might like",game)

main()
