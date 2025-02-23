import random

def roll_dice():
    """Function to roll the dice and return the result."""
    return random.randint(1, 6)

def main():
    """Main function to control the flow of the dice rolling game."""
    while True:
        print("Rolling Dice...")

        # Rolling the dice
        result = roll_dice()
        print(f"The value is: {result}")

        # Asking user to roll the dice again or quit
        repeat = input("Roll Dice again? (y/n): ").strip().lower()

        # Check if user wants to quit
        if repeat != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
