import phonenumbers
from phonenumbers import carrier, geocoder
from tabulate import tabulate

def phone_number_scanner(phone_number):
    phone_no = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(phone_no, "en")
    supplier = carrier.name_for_number(phone_no, "en")
    info = [["Country", "Supplier"], [description, supplier]]
    data = str(tabulate(info, headers="firstrow", tablefmt="github"))
    return data

if __name__ == "__main__":
    phone_no = input("Enter Phone no: ")
    print(phone_number_scanner(phone_no))