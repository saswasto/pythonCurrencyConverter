import requests

def get_exchange_rates(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates']

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    if from_currency in exchange_rates and to_currency in exchange_rates:
        conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Currency not found in exchange rates data"

def main():
    base_currency = input("Enter the base currency code (e.g., USD): ").upper()
    exchange_rates = get_exchange_rates(base_currency)

    if not exchange_rates:
        print("Failed to fetch exchange rates. Please check your input or try again later.")
        return

    print("Available currencies:")
    for currency in exchange_rates.keys():
        print(currency)

    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    amount = float(input("Enter the amount to convert: "))
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)

    if isinstance(converted_amount, str):
        print(converted_amount)
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
