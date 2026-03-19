# pattern 24
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
