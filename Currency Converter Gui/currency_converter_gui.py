import tkinter as tk
from tkinter import font, ttk
import requests


class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("380x360")

        self.api_key = 'cur_live_hwR3cJRG0Ebv48FXKp62KpcvOjmNgKdSaHhw62uR'

        # Create a frame for the title with a blue background
        self.title_frame = tk.Frame(root, bg="blue")
        self.title_frame.pack(fill="both")

        # Setting the font for H1 title
        self.h1_font = font.Font(family="Helvetica", size=22, weight="bold")

        # Creating and placing the H1 title inside the title frame
        self.title_label = tk.Label(
            self.title_frame, text="CURRENCY CONVERTER", font=self.h1_font, bg="blue", fg="white")
        self.title_label.pack(pady=20)

        # Creating and placing the output label with black border
        self.output_label = tk.Label(root, text="Output will be displayed here",
                                     borderwidth=2, relief="solid", width=50, height=5, wraplength=400)
        self.output_label.pack(pady=10, padx=20)

        # Frame for dropdowns
        self.dropdown_frame = tk.Frame(root)
        self.dropdown_frame.pack(pady=10)

        # Dropdown list of currencies
        self.currencies = ['ADA', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AVAX', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BNB', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DOT', 'DZD', 'EGP', 'ERN', 'ETB', 'ETH', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD',
                           'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTC', 'LTL', 'LVL', 'LYD', 'MAD', 'MATIC', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'XRP', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']

        # Dropdown for 'From' currency
        self.from_label = tk.Label(
            self.dropdown_frame, text="From:", font=("Helvetica", 12))
        self.from_label.grid(row=0, column=0, padx=10, pady=5)

        self.from_currency = tk.StringVar()
        self.from_currency.set("USD")  # Default value
        self.from_dropdown = ttk.Combobox(
            self.dropdown_frame, textvariable=self.from_currency, values=self.currencies, state="readonly", width=20)
        self.from_dropdown.grid(row=1, column=0, padx=10, pady=5)

        # Dropdown for 'To' currency
        self.to_label = tk.Label(
            self.dropdown_frame, text="To:", font=("Helvetica", 12))
        self.to_label.grid(row=0, column=1, padx=10, pady=5)

        self.to_currency = tk.StringVar()
        self.to_currency.set("EUR")  # Default value
        self.to_dropdown = ttk.Combobox(
            self.dropdown_frame, textvariable=self.to_currency, values=self.currencies, state="readonly", width=20)
        self.to_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Input field for value to convert
        self.value_label = tk.Label(
            root, text="Enter value:", font=("Helvetica", 12))
        self.value_label.pack(pady=5)

        self.value_entry = tk.Entry(root, width=58)
        self.value_entry.pack()

        # Convert button
        self.convert_button = tk.Button(
            root, text="Convert", command=self.convert, width=25, height=2)
        self.convert_button.pack(pady=10)

    def fetch_exchange_rates(self):
        url = "https://api.currencyapi.com/v3/latest"
        params = {
            'apikey': self.api_key,
            'currencies': ','.join(self.currencies)
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                return data['data']
            else:
                print("Error: 'data' key not found in API response.")
                print(data)
                return None
        else:
            print(f"Failed to fetch data: {
                  response.status_code} - {response.text}")
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        rates_data = self.fetch_exchange_rates()
        if rates_data:
            rates = {currency: info['value']
                     for currency, info in rates_data.items()}
            if from_currency in rates and to_currency in rates:
                return amount * rates[to_currency] / rates[from_currency]
            else:
                print(f"Currency not found in rates: {
                      from_currency}, {to_currency}")
                return None
        else:
            print("Failed to fetch exchange rates")
            return None

    def convert(self):
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        value = self.value_entry.get()

        try:
            amount = float(value)
            converted_amount = self.convert_currency(
                amount, from_currency, to_currency)
            if converted_amount is not None:
                result = f"{amount} {from_currency} = {
                    converted_amount:.2f} {to_currency}"
            else:
                result = "Conversion failed."
        except ValueError:
            result = "Invalid input value. Please enter a number."

        self.output_label.config(text=result)


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
