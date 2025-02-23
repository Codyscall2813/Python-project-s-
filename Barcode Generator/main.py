import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(data, filename):
    # Create a Code128 barcode
    code128 = barcode.get_barcode_class('code128')
    barcode_instance = code128(data, writer=ImageWriter())

    # Save the barcode as an image in the specified directory
    try:
        barcode_instance.save(filename)
        print(f'Barcode saved as {filename}.png')
    except Exception as e:
        print(f'Failed to save barcode: {e}')

def main():
    # Ensure the directory exists
    directory = 'Collection/barcode generator'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Take input from the user
    data = input('Enter the data for the barcode: ')
    filename = os.path.join(directory, 'barcode')  # Full path for saving

    # Generate and save the barcode
    generate_barcode(data, filename)

if __name__ == "__main__":
    main()
