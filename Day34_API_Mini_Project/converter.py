from api import get_rates

def convert_currency(amount, base, target):
    rates = get_rates(base)

    if not rates:
        return None

    if target not in rates:
        print("Invalid target currency!")
        return None

    converted = amount * rates[target]
    return round(converted, 2)
