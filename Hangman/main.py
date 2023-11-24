import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'melon', 'peach']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def play_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        else:
            print("Good guess!")

        display = display_word(word_to_guess, guessed_letters)
        print(display)

        if display_word(word_to_guess, guessed_letters).replace('_ ', '') == word_to_guess:
            print("Congratulations! You guessed the word!")
            break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

play_game()
