#pattern 12
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
