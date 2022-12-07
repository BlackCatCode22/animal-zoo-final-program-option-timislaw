class Animal:
# temporary habitat -- make so species determines which habitat is placed into; hyena habitat, lion habitat, etc
    
    def __init__(self, name, age, sex, color, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
   
# just testing code
# bozoMonke = Animal('Bozo', 'Monkey', 45, 'Male', 'Black', '10 oz')
# yoloMonke = Animal('Yolo', 'Monkey', 42, 'Female', 'Brown', '9 oz')

# print(bozoMonke)
# print(yoloMonke)

# print(bozoMonke == yoloMonke)

# add habitat and species to these classes
class Hyena(Animal):
    species = 'Hyena'
    habitat = 'Hyena Habitat'

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"
    
class Lion(Animal):
    species = 'Lion'
    habitat = 'Lion Habitat'

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

class Bear(Animal):
    species = 'Bear'
    habitat = 'Bear Habitat'

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

class Tiger(Animal):
    species = 'Tiger'
    habitat = 'Tiger Habitat'

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"

# new_bear = Bear('Bearly', 3, 'Male', 'Black', '120 lbs')
# print(new_bear)

f = open('arrivingAnimals.txt', 'r')

animals = [line.strip() for line in f]

animals = tuple(animals)

print(animals[15])

counter = 0

for animal in animals:
    counter = counter + 1
    # start organizing info into different classes assigning id's
    if type(animal[counter]) == str:
        print('admitted', counter)