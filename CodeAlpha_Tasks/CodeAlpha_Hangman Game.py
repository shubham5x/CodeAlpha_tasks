#        HangMan Game using Python



import random


# List of words

words = [
          "apple", "orange", "python", "java",
          "student", "school", "college", "computer"
]


# Hangman stages

hangman_stages = [
    # 6 lives
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,

    # 5 lives
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,

    # 4 lives
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    # 3 lives
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    # 2 lives
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    # 1 life
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    # 0 lives
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Choose random word

word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to HangMan Game🎮!!")

while attempts > 0:

    # Display current word

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)



    # Check win before asking again

    if "_" not in display_word:
        print("\nCongratulations🥳 You won!")
        print("The word was:", word)
        break

    guess = input("\nGuess a letter: ").lower()



    # Input validation

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if not guess.isalpha():
        print("Please enter a valid alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Attempts left:", attempts)

    print(hangman_stages[6 - attempts])
    print("Guessed letters:", guessed_letters)



# Loss condition

if attempts == 0:
    print(hangman_stages[-1])
    print("\n☠️ You lost!")
    print("The word was:", word)


# code is end here...