year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!")
else:
    # If the conditions for a leap year are not met, it's not a leap year
    print(f"{year} is not a leap year.")
