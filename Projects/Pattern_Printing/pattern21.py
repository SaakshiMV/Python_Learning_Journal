# pattern 21
#         A 
#       A B A 
#     A B C B A 
#   A B C D C B A 
# A B C D E D C B A 
#   A B C D C B A 
#     A B C B A 
#       A B A 
#         A 

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(chr(64 + k), end=" ")
    for l in range(i - 1, 0, -1):
        print(chr(64 + l), end=" ")
    print()
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(chr(64 + k), end=" ")
    for l in range(i - 1, 0, -1):
        print(chr(64 + l), end=" ")
    print()
