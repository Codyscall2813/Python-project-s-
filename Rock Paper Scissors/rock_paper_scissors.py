import random

def get_user_choice():
    while True:
        user_choice = input("Choose one: Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("\nWelcome to Rock, Paper, Scissors!\n")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("\nYou chose:", user_choice.capitalize())
        print("Computer chose:", computer_choice.capitalize())
        print(determine_winner(user_choice, computer_choice))
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break
        print()

if __name__ == "__main__":
    main()