# Example 1: Basic Class
class Person:
    pass
  
p1 = Person()
print(p1)


# Example 2: Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 20)
print(s1.name, s1.age)


# Example 3: Methods
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")
d1 = Dog("Buddy")
d1.bark()


# Example 4: Multiple Objects
class Car:
    def __init__(self, brand):
        self.brand = brand

c1 = Car("Toyota")
c2 = Car("BMW")
print(c1.brand)
print(c2.brand)
