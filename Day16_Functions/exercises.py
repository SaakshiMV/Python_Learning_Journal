# Exercise 1
# Create a function to print your name
def my_name():
    print("xyz")
my_name()

# Exercise 2
# Function to add two numbers
def add(a, b):
    return a + b
print(add(3, 4))

# Exercise 3
# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(10))

# Exercise 4
# Function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}")
greet()
greet("John")

# Exercide 5
# Utility Functions

# 1. Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

# 2. String utility
def format_name(name):
    return name.strip().title()

# 3. List utility
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Testing utilities
print(add(10, 5))
print(format_name("   saakshi   "))
print(get_even_numbers([1, 2, 3, 4, 5, 6]))
