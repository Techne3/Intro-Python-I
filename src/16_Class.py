class Animal:
    def __init__(self, skin_type, species, weight, color, name, environment):
        self.skin_type = skin_type
        self.species = species
        self.weight = weight
        self.color = color
        self.name = name
        self.environment = environment
    def move(self):
        print("???")
    def speak(self):
        print("???")
​
​
class Dog(Animal):
    def __init__(self, name, weight, color):
        super().__init__("fur", "DOG", weight, color, name, "LAND")
    def speak(self):
        print("woof!")
    def move(self):
        print(f"{self.name} walks.")
​
​
​
​
d = Dog("rover", 15, "black")
d2 = Dog("king", 35, "spotted")
​
a = Animal("furry", "DOG", 12, "brown", "fido", "LAND")
