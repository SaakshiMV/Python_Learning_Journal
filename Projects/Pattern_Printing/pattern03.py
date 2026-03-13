# pattern 3
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * *
rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):

    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
        
    # Print stars
    for k in range(2*i - 1):
        print("*", end=" ")
    
    print()
