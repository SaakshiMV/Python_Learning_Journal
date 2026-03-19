# pattern 27
# 1 2 3 4 5 
# 1       5 
# 1       5 
# 1       5 
# 1 2 3 4 5

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  
    for j in range(1, rows + 1):
        if i == 1 or i == rows or j == 1 or j == rows:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
