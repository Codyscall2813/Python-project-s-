import random

# Define the quiz questions, options, and answers
quiz = {
    "question1": {
        "question": "What is the keyword used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    "question2": {
        "question": "Which data type is mutable in Python?",
        "options": ["tuple", "set", "string", "list"],
        "answer": "list"
    },
    "question3": {
        "question": "How do you insert comments in Python code?",
        "options": ["--", "//", "#", "/* */"],
        "answer": "#"
    },
    "question4": {
        "question": "What method is used to remove whitespace from the beginning and end of a string?",
        "options": ["trim", "strip", "remove", "clear"],
        "answer": "strip"
    },
    "question5": {
        "question": "Which function is used to get the length of a list in Python?",
        "options": ["size", "length", "count", "len"],
        "answer": "len"
    },
    "question6": {
        "question": "What is the output of `print(2 ** 3)`?",
        "options": ["6", "8", "10", "16"],
        "answer": "8"
    },
    "question7": {
        "question": "How do you create a new list in Python?",
        "options": ["[]", "list()", "{}"],
        "answer": "[]"
    },
    "question8": {
        "question": "What is the purpose of the 'return' keyword in a function?",
        "options": ["To exit the function", "To return a value", "To start a loop", "To define a function"],
        "answer": "To return a value"
    },
    "question9": {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["^", "exp", "**", "sqrt"],
        "answer": "**"
    },
    "question10": {
        "question": "What does the 'import' keyword do in Python?",
        "options": ["Imports a module", "Creates a variable", "Defines a function", "Starts a loop"],
        "answer": "Imports a module"
    }
}

def check_answer(question, user_answer, score):
    """
    Checks if the user's answer is correct and updates the score.
    Answers are compared in lowercase to ensure case-insensitivity.
    """
    correct_answer = quiz[question]['answer']
    if correct_answer.lower() == user_answer.lower():
        print(f"Correct! Your score is {score + 1}.")
        return True
    else:
        print(f"Wrong! The correct answer was: {correct_answer}.")
        return False

def print_question_with_options(question_id):
    """
    Prints the question and its options.
    """
    details = quiz[question_id]
    print(details['question'])
    options = details['options']
    random.shuffle(options)  # Shuffle options for randomness
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def display_intro_message():
    """
    Displays the introduction message and waits for user input to start the quiz.
    """
    print("Welcome to the Python Coding Quiz!")
    print("Test your knowledge with 10 multiple-choice questions.")
    print("Type the number of your answer or 'skip' to skip a question.")
    input("Press Enter to start the quiz... ")
    print()  # Add a blank line for better readability

def run_quiz():
    """
    Runs the quiz game loop.
    """
    display_intro_message()
    
    score = 0
    for question_id in quiz:
        attempts = 1  # Allow only one attempt per question
        while attempts > 0:
            print_question_with_options(question_id)
            user_input = input("Enter the number of your answer: ")
            if user_input.lower() == "skip":
                print("Question skipped.")
                break
            try:
                answer_index = int(user_input) - 1
                if 0 <= answer_index < len(quiz[question_id]['options']):
                    user_answer = quiz[question_id]['options'][answer_index]
                    if check_answer(question_id, user_answer, score):
                        score += 1
                        break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            attempts -= 1

    print(f"\nYour final score is {score} out of 10!")
    print("\nThank you for playing the Python Coding Quiz! 💻")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
