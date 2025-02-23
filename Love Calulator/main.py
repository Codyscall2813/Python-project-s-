import random
import time

CONSONANTS = "bcdfghjklmnprstvwxyz"
VOWELS = "aeiou"

def count_vowels(name):
    """
    Count the number of vowels in the given name.

    Args:
        name (str): The name to count vowels in.

    Returns:
        int: The total count of vowels in the name.
    """
    return sum(1 for char in name.lower() if char in VOWELS)

def count_consonants(name):
    """
    Count the number of consonants in the given name.

    Args:
        name (str): The name to count consonants in.

    Returns:
        int: The total count of consonants in the name.
    """
    return sum(1 for char in name.lower() if char in CONSONANTS)

def calculate_love_score(name1, name2):
    """
    Calculate a love score based on factors between two names.

    Args:
        name1 (str): First name.
        name2 (str): Second name.

    Returns:
        int: Calculated love score in percentage (0 - 100).
    """
    love_score = 0

    # Compare total vowels in both names
    if count_vowels(name1) == count_vowels(name2):
        love_score += random.randint(10, 30)

    # Compare total consonants in both names
    if count_consonants(name1) == count_consonants(name2):
        love_score += random.randint(20, 40)

    # Compare first letters of both names
    if name1[0].lower() == name2[0].lower():
        love_score += random.randint(10, 30)

    # Compare the lengths of both names
    if len(name1) == len(name2):
        love_score += random.randint(1, 10)

    # Add a random score to the love score
    love_score += random.randint(10, 50)

    return min(love_score, 100)  # Ensure the score does not exceed 100

def display_relationship(name1, name2, love_score):
    """
    Display the relationship details between two names based on the love score.

    Args:
        name1 (str): First name.
        name2 (str): Second name.
        love_score (int): Calculated love score.

    Returns:
        None
    """
    print("Calculating...")
    time.sleep(random.randint(1, 3))
    print(f"{name1} and {name2} have a {love_score}% relationship.")

    if love_score >= 90:
        print("They have an unbreakable relationship that will last forever.")
    elif love_score >= 70:
        print("They have a strong relationship that will most likely lead to a marriage.")
    elif love_score >= 50:
        print("They have a good relationship that can lead to a honeymoon to Paris.")
    else:
        print("They have a weak relationship that could have been a 'match made in heaven'.")

if __name__ == "__main__":
    name1 = input("Please type Name 1:\n")
    name2 = input("Please type Name 2:\n")

    score = calculate_love_score(name1, name2)
    display_relationship(name1, name2, score)
