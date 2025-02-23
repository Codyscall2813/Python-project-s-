import random
import requests
import time

def fetch_words(url):
    """
    Fetches a list of words from a given URL and filters out words with less than 3 characters.
    
    :param url: URL to fetch the word list from
    :return: List of filtered words
    """
    response = requests.get(url)
    response.raise_for_status()
    words = response.text.splitlines()
    
    # Filter words to include only those with length >= 3
    filtered_words = [word for word in words if 3 <= len(word) <= 7]
    
    return filtered_words

def hangman():
    """
    A simple Hangman game where the player has to guess a word by suggesting letters
    within a limited number of attempts.
    """
    # URL to fetch words from
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    words = fetch_words(url)

    # Check if there are enough words to choose from
    if not words:
        print("No words available for the game.")
        return

    # Select a random word from the list
    chosen_word = random.choice(words)
    guessed_letters = set()
    attempts_remaining = 5

    print("\nWelcome to Hangman! Try to guess the word.")

    while attempts_remaining > 0:
        # Display the current state of the word with guessed letters
        displayed_word = ' '.join(letter if letter in guessed_letters else '_' for letter in chosen_word)
        print("\nWord: ", displayed_word)

        # Check if the word is fully guessed
        if '_' not in displayed_word:
            print("Congratulations! You guessed the word:", chosen_word)
            break

        # Get user's guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts_remaining -= 1

        print("Attempts left:", attempts_remaining)

    if attempts_remaining == 0:
        print("Sorry, you ran out of attempts. The word was:", chosen_word)

# Run the Hangman game
print("Hello! Welcome to the Hangman game. Enjoy playing! 😊")
time.sleep(2)
print("Let's get started!")
hangman()
