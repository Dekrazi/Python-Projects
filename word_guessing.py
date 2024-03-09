import random

categories = {
    "fruits": [
        "apple", "banana", "orange", "grape", "melon", "lemon", "berry", "kiwi", "peach", "plum",
        "fig", "pear", "mango", "cherry", "date", "guava", "lychee", "papaya", "lime"
    ],
    "animals": [
        "dog", "cat", "elephant", "lion", "tiger", "giraffe", "zebra", "monkey", "snake", "rabbit",
        "bird", "fish", "shark", "whale", "dolphin", "penguin", "octopus", "crocodile", "frog", "turtle"
    ],
    "colors": [
        "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white",
        "gray", "silver", "gold", "cyan", "magenta", "turquoise", "maroon", "olive", "navy", "teal"
    ],
    "countries": [
        "USA", "Canada", "Australia", "India", "China", "Brazil", "Russia", "Germany", "France", "Japan",
        "Italy", "Mexico", "Spain", "South Korea", "Indonesia", "Turkey", "Saudi Arabia", "Netherlands", "Switzerland", "Argentina"
    ]
}


max_attempts = 15

user = input("Enter your name: ")
category = input("Choose category - fruits, animals, colors, countries: ").lower()

word_list = categories.get(category)
if word_list is None:
    print("Invalid category choice.")
    exit()

while True:
    attempts = 0
    word = random.choice(word_list)
    guessed_letters = set()
    
    while attempts < max_attempts:
        
        display_word = ''.join([letter if letter in guessed_letters else '*' for letter in word])
        print("Current word:", display_word)

        guess = input("Type in a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter: ")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        
        if set(word) <= guessed_letters:
            print("Congratulations! You guessed the word:", word)
            break

        
        if guess in word:
            print(f"The letter {guess} is in the word!")
        else:
            print("The letter {guess} is not in the word.")
            attempts += 1
            print("Attempts remaining:", max_attempts - attempts)
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break

print("Thank you for playing!")


