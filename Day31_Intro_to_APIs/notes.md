# 🌐 Day 31 — Introduction to APIs

## Overview

Welcome to **Day 31 of my 45-Day Python Learning Journey**.

Today I learned about **APIs (Application Programming Interfaces)** and how to fetch **real-world data** using Python.

This is an important step toward building applications that interact with external services.

---

## 🧠 What is an API?

An **API** allows different applications to communicate with each other.

Instead of building everything from scratch, we can request data from external services.

### Examples:

- 🌦️ A weather app gets data from a weather API  
- 💱 A finance app gets currency exchange rates from an API  

---

## 🚀 What I Built

I created a simple Python program that fetches **live currency exchange rates** using an API.

This program sends a request to an API and processes the response.

---

## ⚙️ How APIs Work

1. Send an HTTP request to an API endpoint  
2. The server processes the request  
3. It returns data (usually in JSON format)  
4. The program reads and uses that data  

---

## 🧠 Using the `requests` Library

```python
import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
data = response.json()

print("USD Rate:", data["rates"]["USD"])
print("EUR Rate:", data["rates"]["EUR"])
````

---

## 🧾 Example Output

```
USD Rate: 0.012
EUR Rate: 0.011
```

---

## 📌 What I Learned

Today I learned:

* What APIs are and why they are useful
* How HTTP requests work
* How to use the `requests` library
* How to handle JSON responses
* How to fetch and display real-world data

---

## 💭 Reflection

This was my first step into connecting Python programs with real-world data.

It opened up possibilities to build applications like:

* Weather apps
* Finance trackers
* Data dashboards

Understanding APIs is a major step toward becoming a **full-stack and real-world developer** 🚀
