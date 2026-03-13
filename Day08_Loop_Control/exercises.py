# Exercise 1
# Stop loop when number reaches 7
print("\nExercise 1: ")
for i in range(10):
    if i == 7:
        break
    print(i)


# Exercise 2
# Skip number 5
print("\nExercise 2: ")
for i in range(10):
    if i == 5:
        continue
    print(i)


# Exercise 3
# Find a number in a list
print("\nExercise 3: ")
numbers = [4, 9, 2, 7, 1]

for num in numbers:
    if num == 7:
        print("Number found!")
        break


# Exercise 4
# Print odd numbers only
print("\nExercise 4: ")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
