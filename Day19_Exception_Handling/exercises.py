# Exercise 1
# Handle invalid number input
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")

# Exercise 2
# Handle division by zero
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Exercise 3
# Handle file not found
try:
    with open("file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")

#exercise 4
# Improved Notes App with Exception Handling
while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            note = input("Enter your note: ")
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            print("Note saved!")
        except Exception as e:
            print("Error saving note:", e)

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\nYour Notes:")
                print(file.read())
        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
