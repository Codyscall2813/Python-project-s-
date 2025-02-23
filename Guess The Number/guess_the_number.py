import random


def guess_number_game():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {
                      secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_number_game()
    else:
        print("Thank you for playing!")


# Start the game
guess_number_game()
