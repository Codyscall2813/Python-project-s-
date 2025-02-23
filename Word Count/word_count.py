def count_words_and_characters(text):
    words = text.split()
    word_count = len(words)
    character_count = len(text)

    return word_count, character_count

def main():
    filename = input("Enter the filename (with .txt extension): ")

    try:
        with open(filename, 'r') as file:
            text = file.read()

        word_count, character_count = count_words_and_characters(text)

        print(f"Word count: {word_count}")
        print(f"Character count: {character_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()