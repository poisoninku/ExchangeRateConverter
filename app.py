import requests

# Function to get the exchange rate from the API
def get_exchange_rate(base_currency, target_currency):
    api_key = "36410e9f9ef7202cc437bbb48f5d4fa1"  # Replace with your API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Check if the response is valid and contains conversion rates
        if "conversion_rates" in data and target_currency in data["conversion_rates"]:
            return data["conversion_rates"][target_currency]
        else:
            print(f"Error: {target_currency} not found in conversion rates.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to convert the currency based on the exchange rate
def convert_currency(base_currency, target_currency, amount):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed due to invalid data.")

# Function to handle user inputs and perform the conversion
def main():
    print("=== Welcome to the Currency Converter ===")
    
    # List of supported currencies (ISO 4217 codes)
    currencies = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY", "MXN", "BRL", "CHF", "ZAR"]

    print(f"\nSupported currencies: {', '.join(currencies)}")

    base_currency = input(f"Enter the base currency (e.g., {currencies[0]}): ").upper()
    # Validate if the base currency is supported
    while base_currency not in currencies:
        print("Invalid base currency. Please choose from the supported currencies.")
        base_currency = input(f"Enter the base currency (e.g., {currencies[0]}): ").upper()

    target_currency = input(f"Enter the target currency (e.g., {currencies[1]}): ").upper()
    # Validate if the target currency is supported
    while target_currency not in currencies:
        print("Invalid target currency. Please choose from the supported currencies.")
        target_currency = input(f"Enter the target currency (e.g., {currencies[1]}): ").upper()

    try:
        amount = float(input("Enter the amount to convert: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            if base_currency == target_currency:
                print(f"{amount:.2f} {base_currency} = {amount:.2f} {target_currency} (no conversion needed)")
            else:
                convert_currency(base_currency, target_currency, amount)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

if __name__ == "__main__":
    main()

