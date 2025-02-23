def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32


def main():
    print("Welcome to the Temperature Converter!")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
