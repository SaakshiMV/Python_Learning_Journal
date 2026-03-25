# Exercise 1
# Create two classes with same method
class Bird:
    def sound(self):
        print("Chirp")

class Cow:
    def sound(self):
        print("Moo")

animals = [Bird(), Cow()]
for a in animals:
    a.sound()


# Exercise 2
# Polymorphism with shapes
class Rectangle:
    def area(self):
        print("Rectangle area")

class Triangle:
    def area(self):
        print("Triangle area")

shapes = [Rectangle(), Triangle()]

for s in shapes:
    s.area()
