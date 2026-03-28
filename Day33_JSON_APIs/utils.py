def filter_currencies(data, targets):
    if not data or "rates" not in data:
        return {}

    rates = data["rates"]

    filtered = {}
    for currency in targets:
        if currency in rates:
            filtered[currency] = rates[currency]

    return filtered


def format_output(filtered_data, base):
    print(f"\nExchange Rates (Base: {base})")
    print("-" * 30)

    for currency, value in filtered_data.items():
        print(f"{currency}: {value}")
