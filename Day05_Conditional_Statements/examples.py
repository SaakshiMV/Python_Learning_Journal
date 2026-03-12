# Simple if statement
print("\nif example: ")
age = 20
if age >= 18:
    print("You are an adult")


# if-else example
print("\nif-else example: ")
number = 15
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# if-elif-else example
print("\nif-elif-else example: ")
score = 85
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Grade C")


# Nested condition example
print("\nnested example: ")
age = 22
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
