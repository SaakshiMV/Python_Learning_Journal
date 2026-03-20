# Exercise 1
# Create a function to print your name
def my_name():
    print("Saakshi")
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
