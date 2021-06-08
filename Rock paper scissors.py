win = 0
loss = 0
ai = t[randint(0, 2)]

while True:
    user = input("Choose: Rock, Paper, Scissor")

    if user == ai:
        print("Tie!")
    elif user == "Rock" or user == 'R' or user == "r":
        if ai == "Paper":
            print("You lose!", computer, "can't beat", player)
            loss = loss + 1
        else:
            print("You win!", player, "can beat", computer)
            win = win + 1
    elif user == "Paper" or user == 'P' or user == "p":
        if ai == "Scissors":
            print("You lose!", computer, "can't", player)
            loss = loss + 1
        else:
            print("You win!", player, "can beat", computer)
            win = win + 1
    elif user == "Scissor" or user == 'S' or user == "s":
        if ai == "Rock":
            print("You lose...", computer, "can't beat", player)
            loss = loss + 1
        else:
            print("")
            print("You win!", player, "can beat", computer)
            win = win + 1
    else:
        print("That's not a valid play. Check your spelling!")

    print("")
    print("Scores")
    print("Correct:" + win)
    print("Wrong:" + loss)
    print("")

    loss = input("Do you want to play another game?")
    if quit in ["Yes", "YES", "yes", "Y", "y"]:
        pass
    elif quit in ["NO", "No", "no", "N", "n"]:
        print("Thank you for playing you did great!")
    else:
        break
