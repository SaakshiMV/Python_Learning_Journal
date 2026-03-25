import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
data = response.json()

print("USD Rate:", data["rates"]["USD"])
