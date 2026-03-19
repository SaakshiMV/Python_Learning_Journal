# Exercise 1
# Create a dictionary and print values
person = {
    "name": "Alex",
    "age": 25,
    "city": "Delhi"
}
print(person["name"])

# Exercise 2
# Add a new key
person["job"] = "Engineer"
print(person)

# Exercise 3
# Update value
person["age"] = 26
print(person)

# Exercise 4
# Loop through dictionary
for key, value in person.items():
    print(key, value)

# Exercide 5
# Simple Student Record System
student = {}

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

student["name"] = name
student["marks"] = marks

if marks >= 50:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print("\nStudent Record:")
for key, value in student.items():
    print(key, ":", value)
