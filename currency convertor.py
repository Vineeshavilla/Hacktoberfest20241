import json

# Sample exchange rates (1 unit of base currency = X units of target currency)
exchange_rates = {
    "USD": {"EUR": 0.85, "JPY": 110.0, "INR": 74.0},
    "EUR": {"USD": 1.18, "JPY": 129.0, "INR": 87.0},
    "JPY": {"USD": 0.0091, "EUR": 0.0078, "INR": 0.67},
    "INR": {"USD": 0.013, "EUR": 0.011, "JPY": 1.49},
}

def convert_currency(amount, from_currency, to_currency):
    """Convert the amount from one currency to another."""
    if from_currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {from_currency}")
    if to_currency not in exchange_rates[from_currency]:
        raise ValueError(f"Unsupported conversion from {from_currency} to {to_currency}")
    
    rate = exchange_rates[from_currency][to_currency]
    return amount * rate

def main():
    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("From Currency (USD, EUR, JPY, INR): ").upper()
    to_currency = input("To Currency (USD, EUR, JPY, INR): ").upper()

    try:
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
