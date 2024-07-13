#important note - you can put your api key right here in the 41st line

import requests
def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates'][to_currency]
    else:
        print("Error fetching data.")
        return None

def list_currencies(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for code in data['supported_codes']:
            print(f"{code[0]}: {code[1]}")
    else:
        print("Error fetching data.")

def convert_currency(amount, from_currency, to_currency, api_key):
    rate = get_exchange_rate(api_key, from_currency, to_currency)
    if rate:
        return amount * rate
    else:
        return None

def validate_currency(api_key, currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        codes = [code[0] for code in data['supported_codes']]
        return currency in codes
    else:
        return False

def main():
    api_key = "api key here!" 
    
    while True:
        print("\nCurrency Converter Menu:")
        print("1. Convert Currency")
        print("2. List Supported Currencies")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
            if not validate_currency(api_key, from_currency):
                print(f"Invalid currency code: {from_currency}. Please try again.")
                continue
            
            to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
            if not validate_currency(api_key, to_currency):
                print(f"Invalid currency code: {to_currency}. Please try again.")
                continue
            
            try:
                amount = float(input(f"Enter the amount of {from_currency} to convert: "))
            except ValueError:
                print("Invalid amount. Please enter a numeric value :/")
                continue
            
            converted_amount = convert_currency(amount, from_currency, to_currency, api_key)
            if converted_amount is not None:
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            else:
                print("Conversion failed. Please try again :)")
        
        elif choice == '2':
            print("Supported Currencies-")
            list_currencies(api_key)
        
        elif choice == '3':
            print("Exiting the program, Goodbye! ig")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
