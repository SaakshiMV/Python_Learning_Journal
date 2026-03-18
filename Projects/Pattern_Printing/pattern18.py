#pattern 18
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):
    for j in range(1, i + 1): 
        print(chr(64 + j), end=" ") 
    print()
