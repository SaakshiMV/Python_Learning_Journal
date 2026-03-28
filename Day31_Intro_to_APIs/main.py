from api import get_exchange_rates

rates = get_exchange_rates()

if rates:
    print("Currency Rates (Base: INR)")
    print("--------------------------")
    
    print("USD:", rates.get("USD"))
    print("EUR:", rates.get("EUR"))
    print("GBP:", rates.get("GBP"))
