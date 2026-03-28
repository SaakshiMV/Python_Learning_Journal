import requests

def get_exchange_rates(base="INR"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    
    try:
        response = requests.get(url)
        data = response.json()
        return data["rates"]
    except Exception:
        print("Error fetching data from API")
        return None
