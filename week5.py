# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
    
    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"
    
    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Derived class
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)  # inherit from parent
        self.flight_speed = flight_speed
    
    def use_power(self):
        return f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!"

# Another Derived class
class TechHero(Superhero):
    def __init__(self, name, power, city, gadgets):
        super().__init__(name, power, city)
        self.gadgets = gadgets
    
    def use_power(self):
        return f"{self.name} uses advanced gadgets like {', '.join(self.gadgets)}!"

# Creating objects
hero1 = FlyingHero("SkyGuardian", "Wind Blast", "Metropolis", 800)
hero2 = TechHero("IronBrain", "Super Intelligence", "CyberCity", ["Drone", "Laser Gun", "AI Suit"])

print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())