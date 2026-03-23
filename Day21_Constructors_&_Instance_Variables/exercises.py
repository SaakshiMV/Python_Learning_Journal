# Exercise 1
# Create a class Phone with brand and price
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

p = Phone("Samsung", 30000)
print(p.brand, p.price)


# Exercise 2
# Create a class Rectangle with length and width
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

r = Rectangle(10, 5)
print("Area:", r.length * r.width)


# Exercise 3
# Create a class Movie with default rating
class Movie:
    def __init__(self, name, rating=5):
        self.name = name
        self.rating = rating

m1 = Movie("Inception")
print(m1.name, m1.rating)
