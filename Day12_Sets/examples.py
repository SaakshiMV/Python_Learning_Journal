# Creating sets
numbers = {1, 2, 3, 4}
print(numbers)

# Removing duplicates
duplicate_list = [1, 2, 2, 3, 4, 4]
unique = set(duplicate_list)
print(unique)

# Adding elements
numbers.add(5)
print(numbers)

# Removing elements
numbers.remove(2)
print(numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
