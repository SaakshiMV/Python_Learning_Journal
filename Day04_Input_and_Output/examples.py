# Simple output
print("\nWelcome to Python programming")


# Taking user input
name = input("\nEnter your name: ")
print("Hello", name)


# Input with number conversion
age = int(input("\nEnter your age: "))
print("Next year you will be", age + 1)


# Multiple inputs
city = input("\nEnter your city: ")
print(f"You live in {city}")


# Simple calculator
num1 = int(input("\nEnter first number: "))
num2 = int(input("\nEnter second number: "))

sum_result = num1 + num2
print("Sum:", sum_result)

dif_result = num1 - num2
print("Difference:", dif_result)

mul_result = num1 * num2
print("Multiplication:", mul_result)

div_result = num1 / num2
print("Division:", div_result)
