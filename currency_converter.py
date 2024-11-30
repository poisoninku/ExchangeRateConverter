import requests
def get_exchange_rate(base_currency, target_currency):
    api_key = "1f774b6b79c9bf29e19a5664"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if target_currency in data["conversion_rates"]:
            return data["conversion_rates"][target_currency]
        else:
            print("Invalid target currency code.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
def convert_currency(base_currency, target_currency, amount):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"\n{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed due to invalid data.")
def main():
    print("=== Welcome to the Currency Converter ===")
    print("\nSupported currencies: USD, EUR, GBP, INR, AUD, CAD, JPY, CNY, MXN, BRL, CHF, ZAR, PEN")
    
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    if base_currency not in ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'JPY', 'CNY', 'MXN', 'BRL', 'CHF', 'ZAR', 'PEN']:
        print("Invalid base currency. Please choose from the supported currencies.")
        return
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    if target_currency not in ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'JPY', 'CNY', 'MXN', 'BRL', 'CHF', 'ZAR', 'PEN']:
        print("Invalid target currency. Please choose from the supported currencies.")
        return
    try:
        amount = float(input("Enter the amount to convert: "))
        convert_currency(base_currency, target_currency, amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")

if __name__ == "__main__":
    main()
