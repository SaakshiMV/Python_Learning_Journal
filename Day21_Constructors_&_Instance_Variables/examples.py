# Example 1: Simple constructor
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
print(p1.name)


# Example 2: Multiple attributes
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

c1 = Car("Tesla", 50000)
print(c1.brand, c1.price)


# Example 3: Default value
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

s1 = Student("John")
print(s1.name, s1.age)


# Example 4: Different objects store different data
class Book:
    def __init__(self, title):
        self.title = title

b1 = Book("Python Basics")
b2 = Book("AI Fundamentals")

print(b1.title)
print(b2.title)
