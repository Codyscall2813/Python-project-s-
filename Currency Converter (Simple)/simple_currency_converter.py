import requests


def fetch_exchange_rates():
    url = "https://api.currencyapi.com/v3/latest"
    params = {
        'apikey': 'cur_live_hwR3cJRG0Ebv48FXKp62KpcvOjmNgKdSaHhw62uR',
        'currencies': 'AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTN,BWP,BYN,BYR,BZD,CAD,CDF,CHF,CLF,CLP,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LTL,LVL,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRO,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLL,SOS,SRD,STD,SVC,SYP,SZL,THB,TJS,TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VEF,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPF,YER,ZAR,ZMK,ZMW,ZWL,BTC,ETH,BNB,XRP,SOL,DOT,AVAX,MATIC,LTC,ADA'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            return data['data']
        else:
            print("Error: 'data' key not found in API response.")
            print(data)  # Print the full response for debugging
            return None
    else:
        print(f"Failed to fetch data: {
              response.status_code} - {response.text}")
        return None


def convert_currency(amount, from_currency, to_currency):
    rates_data = fetch_exchange_rates()
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

# Example usage


def main():
    amount = float(input("Enter amount to convert: "))
    from_currency = input("Convert from (e.g., USD): ").upper()
    to_currency = input("Convert to (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} = {
              converted_amount:.2f} {to_currency}")
    else:
        print("Conversion failed.")


if __name__ == "__main__":
    main()
