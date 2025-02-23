import calendar

# Function to convert month name to month number
def month_name_to_number(month_name):
    month_number = list(calendar.month_name).index(month_name)
    return month_number

# Get input from user
date_input = input("Enter Month & Year (e.g., July, 2024): ")

# Split the input into month and year
month_name, year = date_input.split(", ")
year = int(year)

# Convert month name to month number
month_number = month_name_to_number(month_name)

# Print the calendar for the given month and year
print(calendar.month(year, month_number))