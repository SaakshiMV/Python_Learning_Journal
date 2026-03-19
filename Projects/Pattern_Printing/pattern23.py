#pattern 23
#         1   
#       1   1   
#     1   2   1   
#   1   3   3   1   
# 1   4   6   4   1 

rows = int(input("Enter the row size for the pattern: "))
for i in range(rows ):
    num = 1
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i + 1):
        print(num, end="   ")
        num = num * (i - k) // (k + 1)
    print()
