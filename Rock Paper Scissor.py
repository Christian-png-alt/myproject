from random import randint

gameList = ["Rock", "Paper", "Scissor"]
win = 0
losses = 0

while True:
    user = input("Choose: Rock, Paper, Scissor:")
    ai = gameList[randint(0, 2)]

    if user == ai:
        print("Tie!")
    elif user == "Rock" or user == 'R' or user == "r":
        if ai == "Paper":
            print("You lose!")
            loss = losses + 1
        else:
            print("You win!")
            win = win + 1
    elif user == "Paper" or user == 'P' or user == "p":
        if ai == "Scissors":
            print("You lose!")
            loss = losses + 1
        else:
            print("You win!")
            win = win + 1
    elif user == "Scissor" or user == 'S' or user == "s":
        if ai == "Rock":
            print("You lose!")
            loss = losses + 1
        else:
            print("")
            print("You win!")
            win = win + 1
    else:
        print("That's not a valid play. Check your spelling!")

    print("")
    print("Scores")
    print("Correct:" + str(win))
    print("Wrong:" + str(losses))
    print("")

    loss = input("Do you want to play another game? Yes or No?")
    if loss in ["Yes", "YES", "yes", "Y", "y"]:
        pass
    elif loss in ["NO", "No", "no", "N", "n"]:
        print("Thank you for playing you did great!")
        break
    else:
        break
