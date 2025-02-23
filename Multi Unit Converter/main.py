def convert_length(value, from_unit, to_unit):
    length_units = {'meters': 1, 'kilometers': 1000, 'miles': 1609.34, 'feet': 0.3048}
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Unsupported length unit.")
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {'grams': 1, 'kilograms': 1000, 'pounds': 453.592}
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Unsupported weight unit.")
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    raise ValueError("Unsupported temperature unit.")

def main():
    print("Unit Converter")
    print("1: Length")
    print("2: Weight")
    print("3: Temperature")

    choice = input("Choose the type of conversion (1/2/3): ")

    if choice == '1':
        value = float(input("Enter value: "))
        from_unit = input("From unit (meters, kilometers, miles, feet): ").lower()
        to_unit = input("To unit (meters, kilometers, miles, feet): ").lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    elif choice == '2':
        value = float(input("Enter value: "))
        from_unit = input("From unit (grams, kilograms, pounds): ").lower()
        to_unit = input("To unit (grams, kilograms, pounds): ").lower()
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    elif choice == '3':
        value = float(input("Enter value: "))
        from_unit = input("From unit (celsius, fahrenheit, kelvin): ").lower()
        to_unit = input("To unit (celsius, fahrenheit, kelvin): ").lower()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
