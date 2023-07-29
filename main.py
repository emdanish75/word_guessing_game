import random

# List of words from different categories
word = [
    "New York", "London", "Paris", "Tokyo", "Sydney", "Berlin", "Rome", "Madrid", "Moscow", "Beijing",
    "apple", "banana", "orange", "grape", "kiwi", "pear", "strawberry", "watermelon", "mango", "pineapple",
    "chair", "table", "lamp", "mirror", "clock", "umbrella", "globe", "brush", "wallet", "pillow",
    "moon", "star", "comet", "satellite", "planet", "rocket", "astronaut", "galaxy", "nebula", "telescope",
    "pizza", "hamburger", "pasta", "sushi", "ice cream", "cake", "chocolate", "sandwich", "salad", "pancake"
]


# Function to get the user's choice to play again
def play_again():
    while True:
        choice = input("\nDo you want to play again? (Y/N): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")


# Main game loop: continue until the user decides not to play again
while True:
    # Randomly choose a word from the list
    chosen_word = random.choice(word)
    length = len(chosen_word)
    blanks = "_" * length

    # Determine the category of the chosen word
    category = "Unknown"
    if chosen_word in word[:10]:
        category = "City"
    elif chosen_word in word[10:20]:
        category = "Fruit"
    elif chosen_word in word[20:30]:
        category = "Home Article"
    elif chosen_word in word[30:40]:
        category = "Space object"
    elif chosen_word in word[40:]:
        category = "Food Item"

    # Display the category hint to the user
    print("\nHint: " + category)

    lives = 5  # Initialize the lives to the maximum number

    # Game loop: continue until the word is guessed or lives run out
    while blanks != chosen_word and lives > 0:
        print("\n")
        # Display the current state of the word with underscores and guessed letters
        print("\t".join(blanks))
        print("Lives remaining:", lives)

        # Get a letter guess from the user and convert it to lowercase
        guess = input("Guess a letter: ").lower()

        # Convert the current state of blanks to a list for updating
        updated_blanks = list(blanks)

        found = False

        # Check if the guessed letter matches any letter in the chosen word
        for i in range(length):
            if guess == chosen_word[i]:
                # If the letter is found, update the corresponding blank with the guessed letter
                updated_blanks[i] = guess
                found = True

        # If the guessed letter is not found in the word, reduce the remaining lives
        if not found:
            lives -= 1

        # Convert the updated_blanks list back to a string
        blanks = "".join(updated_blanks)

    # The game loop ends when the word is guessed or lives run out

    # Display the final state of the word
    print("\t".join(blanks))

    # Check if the user won or lost and print the result
    if blanks == chosen_word:
        print("\nCongratulations! You guessed the word:", chosen_word)
    else:
        print("\nSorry, you ran out of lives. The word was:", chosen_word)

    # Ask the user if they want to play again
    if not play_again():
        break
