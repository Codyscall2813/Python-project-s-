import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr_code(data_to_encode, png_filename="myqr.png"):
    try:
        # Generate QR code
        qr_code = pyqrcode.create(data_to_encode)
        
        # Save the QR code as a PNG file with a scale factor of 6
        qr_code.png(png_filename, scale=6)
        
        # Inform the user of the successful creation
        print(f"QR code successfully created and saved as {png_filename}")
    except Exception as e:
        print(f"An error occurred while creating the QR code: {e}")

def read_qr_code(png_filename="myqr.png"):
    try:
        # Open the image file
        img = Image.open(png_filename)
        
        # Decode the QR code
        decoded_objects = decode(img)
        
        if decoded_objects:
            for obj in decoded_objects:
                print(f"Decoded data: {obj.data.decode('utf-8')}")
        else:
            print("No QR code found in the image.")
    except Exception as e:
        print(f"An error occurred while reading the QR code: {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Generate QR Code")
        print("2. Read QR Code")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            data_to_encode = input("Enter the text or URL you want to generate a QR code for: ")
            generate_qr_code(data_to_encode)
        elif choice == '2':
            png_filename = input("Enter the filename of the QR code image (default is 'myqr.png'): ") or "myqr.png"
            read_qr_code(png_filename)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
