import random

computer = random.choice([-1, 0, 1])
youStr = (
    input("Enter your choice (S for Snake, W for Water, G for Gun): ").strip().upper()
)

youDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youStr not in youDict:
    print("Invalid choice! Please choose S, W, or G.")
else:
    you = youDict[youStr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    else:
        if computer == -1 and you == 1:
            print("You win!")
        elif computer == -1 and you == 0:
            print("You lose!")
        elif computer == 1 and you == 0:
            print("You lose!")
        elif computer == 1 and you == -1:
            print("You lose!")
        elif computer == 0 and you == 1:
            print("You lose!")
        elif computer == 0 and you == -1:
            print("You win!")
        else:
            print("Something went wrong!")
