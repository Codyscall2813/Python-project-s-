import openpyxl
import sys

print("This program writes the data from a CSV file to an Excel file.")
print("Both input and output files must be in the same directory as this Python script.\n")

csv_name = input("Name of the CSV file for input (with the extension): ")
sep = input("Separator of the CSV file: ")
excel_name = input("Name of the Excel file for output (with the extension): ")
sheet_name = input("Name of the Excel sheet for output: ")

try:
    # Load existing Excel workbook or create a new one if it doesn't exist
    wb = openpyxl.load_workbook(excel_name)
    sheet = wb[sheet_name]

    # Open the CSV file for reading
    with open(csv_name, "r", encoding="utf-8") as file:
        # Initialize row and column counters
        row = 1
        column = 1

        # Process each line in the CSV file
        for line in file:
            # Remove newline and split by separator
            line = line.rstrip('\n').split(sep)

            # Write each data item to the Excel sheet
            for data in line:
                sheet.cell(row, column).value = data
                column += 1

            # Move to the next row for the next line of CSV
            column = 1
            row += 1

    # Save changes to the Excel workbook
    wb.save(excel_name)
    print(f"Data successfully written to '{excel_name}' sheet '{sheet_name}'.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit()
