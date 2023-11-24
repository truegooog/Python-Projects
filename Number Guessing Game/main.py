import random

def play_game():
    while True:
        secret_number = random.randint(1, 20)

        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 20. Try to guess it.")

        while True:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print("Congratulations! You guessed the correct number!")
                break
            elif guess < secret_number:
                print("Too low! Try guessing a higher number.")
            else:
                print("Too high! Try guessing a lower number.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
