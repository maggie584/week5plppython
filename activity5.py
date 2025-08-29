# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

class Bicycle(Vehicle):
    def move(self):
        return "Cycling 🚴"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())