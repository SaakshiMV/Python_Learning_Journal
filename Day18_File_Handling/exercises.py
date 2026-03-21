# Exercise 1
# Write your name to a file
with open("name.txt", "w") as file:
    file.write("xyz")

# Exercise 2
# Read and print file content
with open("name.txt", "r") as file:
    print(file.read())

# Exercise 3
# Append a line to file
with open("name.txt", "a") as file:
    file.write("\nLearning Python")

# Exercise 4
# Count number of characters in file
with open("name.txt", "r") as file:
    content = file.read()
    print(len(content))

# Exercises 5
# Simple Notes App
while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Enter your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note saved!")

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
