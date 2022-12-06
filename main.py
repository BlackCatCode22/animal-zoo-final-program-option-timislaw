class Animal:
# temporary habitat -- make so species determines which habitat is placed into; hyena habitat, lion habitat, etc
    
    habitat = 'Zoo'
    def __init__(self, name, species, age, sex, color, weight):
        self.name = name
        self.species = species
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"{self.name} is {self.age} years old. They belong to the habitat: {self.habitat}"
   
# just testing code
# bozoMonke = Animal('Bozo', 'Monkey', 45, 'Male', 'Black', '10 oz')
# yoloMonke = Animal('Yolo', 'Monkey', 42, 'Female', 'Brown', '9 oz')

# print(bozoMonke)
# print(yoloMonke)

# print(bozoMonke == yoloMonke)

# add habitat and species to these classes
class Hyena(Animal):
    pass

class Lion(Animal):
    pass

class Bear(Animal):
    pass

class Tiger(Animal):
    pass

