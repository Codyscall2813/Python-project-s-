def number_to_words(num):
    if num == 0:
        return "zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def convert_chunk(number):
        result = []
        if number >= 100:
            result.append(ones[number // 100] + " hundred")
            number %= 100
        if 10 <= number < 20:
            result.append(teens[number - 10])
        else:
            if number >= 20:
                result.append(tens[number // 10])
                number %= 10
            if number > 0 or not result:
                result.append(ones[number])
        return " ".join(result).strip()

    if num < 0:
        return "minus " + number_to_words(-num)
    
    result = []
    chunk_count = 0
    while num > 0:
        chunk = num % 1000
        if chunk > 0:
            result.append(convert_chunk(chunk) + " " + thousands[chunk_count])
        num //= 1000
        chunk_count += 1
    
    return ", ".join(filter(bool, result[::-1])).strip()

if __name__ == "__main__":
    while True:
        user_input = input("Enter a number to convert to words (or 'q' to quit): ").replace(",", "")
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break
        try:
            num = int(user_input)
            print(f"{num} in words is: {number_to_words(num)}")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break
