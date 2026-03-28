import requests

def fetch_data(base="INR"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        return response.json()

    except Exception:
        return None
