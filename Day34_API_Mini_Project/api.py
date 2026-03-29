import requests

def get_rates(base):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            print("API Error!")
            return None

        data = response.json()
        return data.get("rates", {})

    except Exception:
        print("Failed to connect to API")
        return None
