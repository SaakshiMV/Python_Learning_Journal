#pattern 17
# A 
# A B 
# A B C 
# A B C D 
# A B C D E

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()
