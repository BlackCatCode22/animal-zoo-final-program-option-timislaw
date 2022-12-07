import random

f = open('animalNames.txt', 'r')

# make if/else that takes the lines and puts into a separate name list, hyena names, lion names, etc
names = [line.strip() for line in f]

f.close()

print(names)

def gen_birthday():
    pass

def gen_animal_ID():
    id = random.randint(0, 1000)
    return id

def gen_animal_name():

    if Hyena():
        pass
    elif Bear():
        pass
    elif Lion():
        pass
    else:
        pass

def gen_zoo_habitats(species):
    if species.lowercase() == 'hyena':
        return 'Hyena Habitat'
    elif species.lowercase() == 'lion':
        return 'Lion Habitat'
    elif species.lowercase() == 'bear':
        return 'Bear Habitat'
    elif species.lowercase() == 'tiger':
        return 'Tiger Habitat'
    else:
        return 'Temporary Habitat'

class Animal:
# temporary habitat -- make so species determines which habitat is placed into; hyena habitat, lion habitat, etc
    
    def __init__(self, name, age, sex, color, weight, id=gen_animal_ID):
        self.name = name
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
        self.id = id
   
# just testing code
# bozoMonke = Animal('Bozo', 'Monkey', 45, 'Male', 'Black', '10 oz')
# yoloMonke = Animal('Yolo', 'Monkey', 42, 'Female', 'Brown', '9 oz')

# print(bozoMonke)
# print(yoloMonke)

# print(bozoMonke == yoloMonke)

# add habitat and species to these classes
class Hyena(Animal):
    species = 'Hyena'
    habitat = gen_zoo_habitats(species)

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"
    
class Lion(Animal):
    species = 'Lion'
    habitat = gen_zoo_habitats(species)

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

class Bear(Animal):
    species = 'Bear'
    habitat = gen_zoo_habitats(species)

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

class Tiger(Animal):
    species = 'Tiger'
    habitat = gen_zoo_habitats(species)

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"

# new_bear = Bear('Bearly', 3, 'Male', 'Black', '120 lbs')
# print(new_bear)

f = open('arrivingAnimals.txt', 'r')

animals = [line.strip() for line in f]

f.close()

animals = tuple(animals)

# print(animals[15])

counter = 0

for animal in animals:
    counter = counter + 1
    # start organizing info into different classes assigning id's
    if type(animal[counter]) == str:
        # print('admitted', counter)
        pass

