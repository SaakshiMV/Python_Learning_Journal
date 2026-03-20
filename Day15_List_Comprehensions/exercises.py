# Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# Exercise 2
# Get odd numbers
numbers = list(range(1, 11))
odds = [x for x in numbers if x % 2 != 0]
print(odds)

# Exercise 3
# Convert names to uppercase
names = ["alex", "john", "emma"]
upper_names = [name.upper() for name in names]
print(upper_names)

# Exercise 4
# Filter numbers greater than 50
nums = [10, 60, 30, 80, 90]
result = [x for x in nums if x > 50]
print(result)

# Exercise 5
# Data Transformation Example

# Original data
students = ["alice", "bob", "charlie", "david"]
# Convert to uppercase
upper_students = [name.upper() for name in students]
# Filter names with length > 4
long_names = [name for name in students if len(name) > 4]
print("Uppercase Names:", upper_students)
print("Long Names:", long_names)
