# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f'Waypoint(name={self.name}, lat={self.lat}, lon={self.lon})'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f'Geocache(name={self.name}, difficulty={self.difficulty}, size={self.size}, lat={self.lat}, lon={self.lon})'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.name, waypoint.lat, waypoint.lon)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)


class Animal:
    def __init__(self,skin_type, species, weight, color,name,environment):
        self.skin_type = skin_type
        self.species = species
        self.weight = weight
        self.color = color
        self.name = name
        self.environment = environment

    def move():
    if self.environment == "WATER":
        movement = "swims"
        elif self.environment =="AIR"
        movement = 'flies'
        else:
            movement = 'walks'
    print(f"{name} {movement}")
    def speaks():
         if self.species == "DOG":
        sound = "bark"
        elif self.species =="CAT"
        sound = 'meow'
        else:
            sound = '???'
        print(sound)


class Dog(Animal):
    def __init__ (self, name, weight, color)
    super(). __init__("fur", "DOG", weight, color, name,"LAND")
    def speak(self):
        print("woof!")
    def move(self):
        print(f"{self.name} walks")




d= Dog('rover' 15, 'black')
a = Animal("furry", "DOG", 12, "brown","fido","Land")
