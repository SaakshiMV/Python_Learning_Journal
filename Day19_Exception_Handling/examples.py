# Example 1: Basic try-except
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input!")

# Example 2: Division
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

# Example 3: File handling
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
