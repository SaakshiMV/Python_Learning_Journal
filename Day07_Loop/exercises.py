# Exercise 1
# Print numbers from 1 to 10
print("\n===============exercise1================")
for i in range(1, 11):
    print(i)


# Exercise 2
# Print even numbers from 1 to 20
print("\n===============exercise2================")
for i in range(2, 21, 2):
    print(i)


# Exercise 3
# Calculate sum of numbers from 1 to 10
print("\n===============exercise3================")
total = 0

for i in range(1, 11):
    total += i

print("Total:", total)


# Exercise 4
# Countdown using while loop
print("\n===============exercise4================")
count = 5

while count > 0:
    print(count)
    count -= 1

print("Liftoff!")
