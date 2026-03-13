# pattern 4
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

rows = int(input("Enter the rows : "))
for i in range(rows, 0, -1):
    # for printing spaces
    for j in range(rows - i):
        print(" ", end = " ")
    # for printing '*' symbol
    for k in range(2*i - 1):
        print("*", end = " ")
    print()
