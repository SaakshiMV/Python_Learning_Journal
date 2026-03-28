import requests

def get_rates(base="INR"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"

    try:
        response = requests.get(url, timeout=5)

        # Check status code
        if response.status_code != 200:
            print("Error: Failed to fetch data")
            return None

        data = response.json()

        if "rates" not in data:
            print("Invalid response format")
            return None

        return data["rates"]

    except requests.exceptions.Timeout:
        print("Request timed out!")
    except requests.exceptions.ConnectionError:
        print("No internet connection!")
    except Exception as e:
        print("Unexpected error:", e)

    return None
