def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        #We can't directly use (difficulty == "Difficult" or "Causal") as equality can compare only two terms
        #For multi-term we can rely on "is in list" which will come later
        print ("Enter a valid input for difficulty")
        return
    players = input("Mutiplayer or Single? ")
    if not (players == "Multiplayer" or players == "Single"):
        print ("Enter a valid input for players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Pocker")
    elif difficulty == "Difficult" and players == "Single":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("you might like",game)

main()
