# Creating dictionary
student = {
    "name": "xyz",
    "age": 30,
    "course": "Python"
}
print(student)

# Accessing values
print(student["name"])

# Adding and updating
student["grade"] = "A"
student["age"] = 22
print(student)

# Removing item
student.pop("course")
print(student)

# Looping
for key, value in student.items():
    print(key, ":", value)
