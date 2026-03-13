# Example 1: break statement
print("\nBREAK STATEMENT: ")
for i in range(10):
    if i == 6:
        break
    print(i)


# Example 2: continue statement
print("\nCONTINUE STATEMENT: ")
for i in range(6):
    if i == 3:
        continue
    print(i)


# Example 3: pass statement
print("\nPASS STATEMENT: ")
for i in range(5):
    if i == 2:
        pass
    print(i)


# Example 4: searching in list
print("\nEXAMPLE STATEMENT: ")
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num == 6:
        print("Number found")
        break
