import random, math

# SBC is the Stefan Boltzmann constant, used in calculating luminosity.
SBC = 5.670367 * (10 ** -8)
# g is the gravitational constant
g=6.674 * (10 ** -11)

# Name can be changed later.
# Velocity will later be changed to only allow stable orbits.
# Habitable will later be changed to depend on the star's habitable zone.

class Planet:
    def __init__(self, sun, name, distance):
        self.name = name
        #self.distanceFromStar = float(random.random()*10) # measured in AU
        self.distanceFromStar = distance
        self.velocity = float(random.random()*10) # measured in years
        self.mass = float(random.random()*10) # measured in Earths
        self.radius = float(random.random()*10) # measured in Earths
        self.volume = ((4/3)*math.pi*(self.radius**3))
        self.density = (self.mass)/self.volume
        if self.distanceFromStar > star.habitableZoneInner and self.distanceFromStar < star.habitableZoneOuter:
            isHabitable = True
        else:
            self.isHabitable = False
        self.gravity = "placeholder" # input the gravity calculation
        self.sun = sun


class Star:
    def __init__(self):
        self.name = "Sun"
        self.radius = float(random.randint(10000, 7000000)) # measured in km
        self.temperature = random.randint(2000, 27000) # measured in kelvin
        if self.temperature <= 3500:
            self.color = "Red"
        elif self.temperature > 3500 and self.temperature <= 5000:
            self.color = "Orange"
        elif self.temperature > 5000 and self.temperature <= 8000:
            self.color = "Yellow"
        elif self.temperature > 8000 and self.temperature <= 17500:
            self.color = "Yellow"
        else:
            self.color = "Blue"

        # luminosity is used in calculating the habitable zone of a star
        self.surfaceArea = 4*math.pi*self.radius ** 2
        self.luminosity = SBC*self.surfaceArea*(self.temperature ** 4)
        # THIS IS INCORRECT
        self.habitableZoneInner = math.sqrt(self.luminosity)*0.95
        self.habitableZoneOuter = math.sqrt(self.luminosity)*1.37
