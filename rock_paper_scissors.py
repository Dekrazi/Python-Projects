import random
import time


print(
    "Winning rules of the game ROCK PAPER SCISSORS are :\n"
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissor wins \n"
)
time.sleep(2)
# Enter a continuous loop for the game.
while True:
    print("Choose: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = input("What's your choice? ")

    while choice not in ["1", "2", "3"]:
        choice = input("Enter a valid choice from 1-3: ")

    choice = int(choice)

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    print(f"You choose {choice_name}")

    time.sleep(2)
    print("Now's the computer's turn.")
    time.sleep(2)

    # Generate a random choice for the computer (Rock, Paper, or Scissors).
    comp_choice = random.randint(1, 3)

    # Ensure the computer's choice is different from the user's choice to prevent a draw.
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = "rocK"
    elif comp_choice == 2:
        comp_choice_name = "papeR"
    else:
        comp_choice_name = "scissorS"

    print(f"Computer choose {comp_choice_name}")
    time.sleep(2)
    print(f"\n -== {choice_name} VS {comp_choice_name} ==- \n")

    if choice == comp_choice:
        print("It's a DRAW!")
    elif (
        (choice == 1 and comp_choice == 2)
        or (choice == 2 and comp_choice == 3)
        or (choice == 3 and comp_choice == 1)
    ):
        print("Computer wins!")
    else:
        print("You win!")

    time.sleep(2)
    play_again = input("Do you want to play again? (y/n) ")

    if play_again != "y":
        print("Thanks for playing!")
        exit()
