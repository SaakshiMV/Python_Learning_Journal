# pattern 28
# 1 0 1 0 
# 0 1 0 1 
# 1 0 1 0 
# 0 1 0 1

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if (i + j) % 2 == 0:  
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
