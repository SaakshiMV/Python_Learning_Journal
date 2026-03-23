# Simple Student Manager using OOP
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        try:
            marks = int(input("Enter marks: "))
            student = Student(name, marks)
            students.append(student)
            print("Student added!")
        except ValueError:
            print("Invalid marks!")

    elif choice == "2":
        if not students:
            print("No students added yet.")
        else:
            print("\nStudent List:")
            for s in students:
                s.display()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
