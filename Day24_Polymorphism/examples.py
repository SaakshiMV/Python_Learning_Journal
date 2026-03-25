# Example 1: Different classes, same method
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()


# Example 2: Inheritance + overriding
class Shape:
    def area(self):
        print("Calculating area")

class Square(Shape):
    def area(self):
        print("Area of square")

class Circle(Shape):
    def area(self):
        print("Area of circle")

shapes = [Square(), Circle()]

for shape in shapes:
    shape.area()
