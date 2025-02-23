from textblob import TextBlob

def check_and_correct_spelling(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    print("Original Text:\n", content)

    # Correct the spelling using TextBlob
    blob = TextBlob(content)
    corrected_blob = blob.correct()
    corrected_text = str(corrected_blob)

    # Finding and displaying corrections made
    print("\nCorrections:")
    original_words = content.split()
    corrected_words = corrected_text.split()
    correction_count = 0

    for original, corrected in zip(original_words, corrected_words):
        if original != corrected:
            print(f"Incorrect: {original} -> Corrected: {corrected}")
            correction_count += 1

    print(f"\nNumber of corrections made: {correction_count}")

    # Only display and save corrected text if corrections were made
    if correction_count > 0:
        print("\nCorrected Text:\n", corrected_text)
        corrected_file_path = file_path.replace('.txt', '_corrected.txt')
        with open(corrected_file_path, 'w') as file:
            file.write(corrected_text)
        print(f"\nCorrected text has been saved to: {corrected_file_path}")
    else:
        print("\nNo corrections were necessary.")

# Main function to execute the code
def main():
    file_path = input("Enter the path of the text file to check for spelling mistakes: ").strip()
    check_and_correct_spelling(file_path)

if __name__ == "__main__":
    main()
