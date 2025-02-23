import random
import time
from os import system

class BColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

choices = ["s", "w", "g"]

def clear_screen():
    system("cls")

def print_colored(message, color):
    print(color + message + BColors.ENDC)

def get_user_input(prompt):
    return input(prompt).strip().lower()

def play_game():
    score = 0
    for i in range(10):
        comp_choice = random.choice(choices)
        user_choice = get_user_input("Type s for snake, w for water, or g for gun: ")

        if user_choice not in choices:
            print_colored("Invalid input, please try again.", BColors.WARNING)
            continue

        if user_choice == comp_choice:
            print_colored("It's a draw! Play again.", BColors.HEADER)
        elif (user_choice == "s" and comp_choice == "g") or \
             (user_choice == "w" and comp_choice == "s") or \
             (user_choice == "g" and comp_choice == "w"):
            print_colored(f"It's {user_choice} vs {comp_choice}. You lose!", BColors.FAIL)
        else:
            print_colored(f"It's {user_choice} vs {comp_choice}. You win!", BColors.OKGREEN)
            score += 1

        print(f"{9 - i} matches left")

    print(f"Your score is {score} out of 10")
    time.sleep(2)

    if score > 5:
        print_colored("Woooh!!!!!!! Congratulations you won", BColors.OKGREEN + BColors.BOLD)
    elif score == 5:
        print_colored("Game draws!!!!!!!", BColors.HEADER)
    else:
        print_colored("You lose!!! Better luck next time", BColors.FAIL + BColors.BOLD)

def main():
    clear_screen()
    print_colored("Welcome to the game 'Snake-Water-Gun'.", BColors.OKBLUE + BColors.BOLD)
    while True:
        user_response = get_user_input("Wanna play? Type Y or N: ").capitalize()
        if user_response == "N":
            print("Ok, bye! See you later.")
            break
        elif user_response == "Y":
            print("There will be 10 matches, and the one who wins more matches will win. Let's start.")
            play_game()
            break

if __name__ == "__main__":
    main()
