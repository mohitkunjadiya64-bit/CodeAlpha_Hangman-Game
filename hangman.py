import random

# List of words
words = ["apple", "tiger", "house", "robot", "plant"]

# Select random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("===== HANGMAN GAME =====")

while incorrect_guesses < max_incorrect:

    # Display current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_incorrect - incorrect_guesses)

    # Win condition
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check letter
    if guess in word:
        print("Correct Guess!")
    else:
        incorrect_guesses += 1
        print("Wrong Guess!")

# Lose condition
if incorrect_guesses == max_incorrect:
    print("\nGame Over!")
    print("The word was:", word)