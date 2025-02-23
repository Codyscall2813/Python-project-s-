import random
import time

# List of sentences for the typing test
sentences = [
    "This is a typing test.",
    "Type the sentence above this one.",
    "The quick brown fox jumps over the lazy dog.",
    "I love to type because it is so much fun!",
    "Type as fast as you can without making mistakes.",
    "The rain in Spain falls mainly on the plain.",
    "The sun rises in the east and sets in the west.",
    "Programming is a valuable skill in the modern world.",
    "Practice makes perfect, especially in typing.",
    "A journey of a thousand miles begins with a single step.",
    "She sells seashells by the seashore.",
    "Consistency is key to improving typing speed.",
    "Reading books can expand your vocabulary.",
    "Never stop learning, because life never stops teaching.",
    "Hard work beats talent when talent doesn't work hard."
]

# Initialize best scores list
best_scores = []

def run_test(sentences, num_sentences=5):
    # Randomly select a subset of sentences
    selected_sentences = random.sample(sentences, num_sentences)
    
    # Shuffle the selected sentences
    random.shuffle(selected_sentences)

    # Start the timer
    start_time = time.time()

    # Initialize score and word count
    score = 0
    word_count = 0

    # Iterate through each selected sentence
    for sentence in selected_sentences:
        # Display the sentence to be typed
        print("\nType the following sentence:")
        print(sentence)

        # Get the user's input
        typed_sentence = input("Your input: ")

        # Split the sentence into words
        words = sentence.split()

        # Update word count
        word_count += len(words)

        # Check if the input is correct
        if typed_sentence == sentence:
            # Increment score
            score += 1
            print("\033[92mCorrect!\033[0m")  # Success message in green
        else:
            print("\033[91mIncorrect.\033[0m")  # Error message in red

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Calculate words per minute (WPM)
    wpm = word_count / (elapsed_time / 60)

    # Print results
    print(f"\nYou scored {score} out of {num_sentences} in {elapsed_time:.2f} seconds!")
    print(f"Your WPM is {wpm:.2f}")

    # Add score to best scores list
    best_scores.append(score)

def display_best_scores():
    # Display the best scores
    print("\nBest scores:")
    if best_scores:
        for score in sorted(best_scores, reverse=True):
            print(score)
    else:
        print("No scores recorded.")

# Run the typing test with a specified number of sentences
run_test(sentences, num_sentences=5)

# Display best scores
display_best_scores()
