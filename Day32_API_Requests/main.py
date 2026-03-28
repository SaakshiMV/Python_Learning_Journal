from api import get_rates

base = input("Enter base currency (default INR): ").upper() or "INR"

rates = get_rates(base)

if rates:
    print(f"\nRates for {base}:")
    print("----------------------")

    while True:
        target = input("\nEnter currency (or 'exit'): ").upper()

        if target == "EXIT":
            break

        if target in rates:
            print(f"{target}: {rates[target]}")
        else:
            print("Currency not found!")
