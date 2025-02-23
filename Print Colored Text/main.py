import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init(autoreset=True)

# Define a function to print a styled message
def print_colored_message(fore_color, back_color, message):
    print(fore_color + back_color + message)

# Example usage
print_colored_message(Fore.BLUE, Back.YELLOW, "Python is a versatile programming language.")
print_colored_message(Fore.YELLOW, Back.BLUE, "It supports multiple programming paradigms.")
print_colored_message(Back.CYAN, Fore.BLACK, "Python has a vast standard library.")
print_colored_message(Fore.RED, Back.GREEN, "Many open-source projects are written in Python.")
print_colored_message(Back.CYAN, Fore.BLACK, "Make sure to follow @pycode.hubb to level up your Python skills with our informative posts!")
