# 📊 Day 33 — Working with JSON APIs

## Overview

Welcome to **Day 33 of my 45-Day Python Learning Journey**.

Today I focused on working deeply with **JSON data returned from APIs**.

Instead of just printing raw API responses, I learned how to:

- 🔍 Filter data  
- 🎯 Extract useful values  
- 🧱 Structure data for better usage  

This is a crucial step in turning raw data into meaningful information.

---

## 🧠 Key Concepts

- 📦 JSON parsing  
- 🔎 Data filtering  
- 🎯 Selecting specific fields  
- 🔄 Transforming API responses  

---

## 🚀 What I Built

I created a Python program that:

- Fetches currency data from an API  
- Filters only selected currencies  
- Formats the output in a clean and readable way  

---

## ⚙️ Working with JSON Data

### 1️⃣ Parsing JSON

```python
data = response.json()
````

This converts API response into a Python dictionary.

---

### 2️⃣ Extracting Nested Data

```python id="3bq8pv"
rates = data["rates"]
usd = rates["USD"]
eur = rates["EUR"]
```

---

### 3️⃣ Filtering Required Data

```python id="6n0t9f"
selected = ["USD", "EUR", "GBP"]

for currency in selected:
    print(currency, ":", rates.get(currency))
```

---

### 4️⃣ Formatting Output

```python id="u3rm2x"
for currency, value in rates.items():
    print(f"{currency}: {value:.3f}")
```

---

## 📌 What I Learned

Today I learned:

* How to work with JSON data effectively
* How to extract nested values from dictionaries
* How to filter only useful data
* How to transform raw API responses into structured output
* How to write cleaner data-handling logic

---

## 💭 Reflection

Today made one thing very clear:

👉 Working with APIs is mostly about **handling JSON efficiently**.

The better I understand data structures like dictionaries and lists, the more powerful my applications become.

This is a big step toward building **data-driven and real-world applications** 🚀
