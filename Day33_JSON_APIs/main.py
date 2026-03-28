from api import fetch_data
from utils import filter_currencies, format_output

base = input("Enter base currency (default INR): ").upper() or "INR"

data = fetch_data(base)

if not data:
    print("Failed to fetch data.")
else:
    targets = input("Enter currencies (comma separated, e.g. USD,EUR,GBP): ")
    target_list = [c.strip().upper() for c in targets.split(",")]

    filtered = filter_currencies(data, target_list)
    format_output(filtered, base)
