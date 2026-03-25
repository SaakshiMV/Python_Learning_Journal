# Exercise 1
# Create parent and child class
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    pass

c = Car()
c.start()


# Exercise 2
# Add new method in child class
class Bike(Vehicle):
    def ride(self):
        print("Riding bike")

b = Bike()
b.start()
b.ride()


# Exercise 3
# Override method
class Truck(Vehicle):
    def start(self):
        print("Truck started")

t = Truck()
t.start()
