# Exercise 1
# Write your name to a file
with open("name.txt", "w") as file:
    file.write("xyz")

# Exercise 2
# Read and print file content
with open("name.txt", "r") as file:
    print(file.read())

# Exercise 3
# Append a line to file
with open("name.txt", "a") as file:
    file.write("\nLearning Python")

# Exercise 4
# Count number of characters in file
with open("name.txt", "r") as file:
    content = file.read()
    print(len(content))
