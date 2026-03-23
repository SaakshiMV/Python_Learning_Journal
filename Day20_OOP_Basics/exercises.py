# Exercise 1
# Create a class Laptop with brand and price
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("HP", 50000)
print(l1.brand, l1.price)


# Exercise 2
# Create a class Circle with method to calculate area
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())


# Exercise 3
# Create a class Employee with method display details
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

e1 = Employee("John", 40000)
e1.display()
