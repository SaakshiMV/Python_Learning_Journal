# Exercise 1
# Create a class with private variable
class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

p = Person(21)
print(p.get_age())


# Exercise 2
# Update value using method
class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def show(self):
        print(self.__count)

c = Counter()
c.increment()
c.increment()
c.show()


# Exercise 3
# Prevent invalid values
class Product:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")

    def get_price(self):
        return self.__price

p = Product(100)
p.set_price(-50)
print(p.get_price())
