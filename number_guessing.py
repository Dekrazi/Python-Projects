from random import randint
# Number guessing game

# get range from user
try:
    range_start = int(input("What's the start number? "))
    range_end = int(input("What's the end number? "))
    random_number = randint(range_start, range_end)
except ValueError:
    print("Enter a valid number: ")

# set guesses counter
guesses = 0

# set up while loop
while True:
    # ask user for a guess
    try:
        user_guess = int(input("Guess the number! "))
    except ValueError:
        print("Enter a valid number.")
        continue
    
    guesses += 1
    # compare guess to generated number and verufy
    if random_number == user_guess:
        print(f"Great job, you guessed the number {random_number} in {guesses} guesses.")
        break
    elif random_number > user_guess:  
        print("You guessed too low, try again! ")
    else:
        print("You guessed too high, try again! ")


