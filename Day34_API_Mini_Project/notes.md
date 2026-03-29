# 💱 Day 34 — API Mini Project (Currency Converter CLI)

## Overview

Welcome to **Day 34 of my 45-Day Python Learning Journey**.

Today I built a **Currency Converter CLI Tool** using:

- 🌐 APIs (real-time exchange rates)  
- 📦 JSON data handling  
- 💻 Command Line Interface (CLI)  

This project combines multiple concepts into a **practical, real-world application**.

---

## 🚀 Features

- 💱 Convert currency in real-time  
- 🌍 Supports multiple currencies  
- 📡 Uses live API data  
- 🛡️ Error handling included  

---

## ⚙️ Command Usage

### Convert Currency

```bash
python main.py convert <amount> <from_currency> <to_currency>
````

---

## 📌 Example

```bash
python main.py convert 100 INR USD
```

---

## 🧠 How It Works

1. Takes input from command-line arguments
2. Sends a request to a currency exchange API
3. Receives data in JSON format
4. Extracts the required exchange rate
5. Calculates and displays the converted amount

---

## 🧩 Sample Implementation

```python
import sys
import requests

amount = float(sys.argv[2])
base = sys.argv[3].upper()
target = sys.argv[4].upper()

url = f"https://api.exchangerate-api.com/v4/latest/{base}"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"].get(target)

        if rate:
            converted = amount * rate
            print(f"{amount} {base} = {converted:.2f} {target}")
        else:
            print("Invalid target currency")

    else:
        print("API Error:", response.status_code)

except requests.exceptions.RequestException:
    print("Network error occurred")
```

---

## 📌 What I Learned

Today I learned:

* How to combine APIs, JSON, and CLI into one project
* How to build real-world command-line tools
* How to structure multi-file Python applications
* How to handle API errors effectively
* How to process and display live data

---

## 💭 Reflection

This project feels like a **real utility tool** that can be used in daily life.

It brings together multiple concepts into one cohesive system, making my understanding of Python much stronger.

This is a big step toward building **practical and production-level applications** 🚀
