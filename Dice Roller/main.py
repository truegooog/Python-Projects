import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Roller!")
    while True:
        input("Press Enter to roll the dice")
        roll_result = roll_dice()
        print(f"You rolled: {roll_result}")

if __name__ == "__main__":
    main()
