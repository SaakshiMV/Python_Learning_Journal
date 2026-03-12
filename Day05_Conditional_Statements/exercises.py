# Exercise 1
# Check if a number is positive or negative
print("\nCheck if a number is positive or negative": )
number = -5
if number > 0:
    print("Positive")
else:
    print("Negative")

#======================================================
# Exercise 2
# Check if a number is even or odd
print("\nCheck if a number is even or odd")
num = 12
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#======================================================
# Exercise 3
# Determine grade based on marks
print("\nDetermine grade based on marks")
marks = 78
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#======================================================
# Exercise 4
# Check voting eligibility
print("\nCheck voting eligibility")
age = 19
citizen = True
if age >= 18 and citizen:
    print("Eligible to vote")
else:
    print("Not eligible")
