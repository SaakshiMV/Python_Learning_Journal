#pattern 1
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows):
    print(i * "* ")
