# Example 1: Basic inheritance
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


# Example 2: Adding new method
class Cat(Animal):
    def meow(self):
        print("Meow")

c = Cat()
c.speak()
c.meow()


# Example 3: Method overriding
class Bird(Animal):
    def speak(self):
        print("Chirp")

b = Bird()
b.speak()
