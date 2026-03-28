# 🛡️ Day 32 — Making API Requests (Robust Handling)

## Overview

Welcome to **Day 32 of my 45-Day Python Learning Journey**.

Today I improved my API-based program by making it more **robust and reliable**.

I focused on handling:

- ❌ Errors  
- 🔢 Status codes  
- 👤 User input  

These improvements make the application closer to **real-world production systems**.

---

## 🧠 Key Concepts

### 1️⃣ Status Codes

When making API requests, servers respond with status codes:

- **200 → Success**  
- **404 → Not Found**  
- **500 → Server Error**  

Checking these ensures the program behaves correctly.

```python
if response.status_code == 200:
    print("Request successful")
else:
    print("Error:", response.status_code)
````

---

### 2️⃣ Error Handling

Handled common issues like:

* No internet connection
* Invalid API responses
* Server errors

```python
import requests

try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
    data = response.json()
except requests.exceptions.RequestException:
    print("Network error occurred")
```

---

### 3️⃣ Handling User Input

Users can now:

* Choose a base currency
* Request specific currency rates

```python
base = input("Enter base currency: ").upper()
target = input("Enter target currency: ").upper()
```

---

## ⚙️ Improved API Request Example

```python id="z6c0u7"
import requests

base = input("Base currency: ").upper()
target = input("Target currency: ").upper()

try:
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"{target} Rate:", data["rates"].get(target, "Not Found"))
    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException:
    print("Failed to connect to API")
```

---

## 📌 What I Learned

Today I learned:

* How to check API response status codes
* How to handle exceptions properly
* How to write safer and more reliable API code
* How to improve user interaction with inputs
* How real-world applications handle failures

---

## 💭 Reflection

This upgrade made my API program much more **stable and realistic**.

Instead of assuming everything works perfectly, I now handle failures and edge cases.

This is a crucial step toward building **production-ready applications** 🚀
