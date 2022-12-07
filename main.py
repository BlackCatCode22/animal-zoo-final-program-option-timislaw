import random

f = open('animalNames.txt', 'r')

# make if/else that takes the lines and puts into a separate name list, hyena names, lion names, etc
names = [line.strip() for line in f]

f.close()
counter = 0

clean_names = []
cleaner_names = []

for line in names:
    if ',' in line:
        clean_names.append(line)
    
for index in clean_names:
    cleaner_names.extend(word for word in index.split() if ',' in word)

counter = 0

# use strip method to clean up each available name 
cleaner_names = [s.strip(',') for s in cleaner_names]
print(cleaner_names)

def gen_birthday():
    pass

def gen_animal_ID():
    id = random.randint(0, 1000)
    return id



class Animal:
# temporary habitat -- make so species determines which habitat is placed into; hyena habitat, lion habitat, etc
    
    def __init__(self, age=0, sex='Male', color='N/A', weight='1oz', id=gen_animal_ID()):
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
        self.id = id

# add habitat and species to these classes

def gen_zoo_habitats(species):
    if species.lower() == 'hyena':
        return 'Hyena Habitat'
    elif species.lower() == 'lion':
        return 'Lion Habitat'
    elif species.lower() == 'bear':
        return 'Bear Habitat'
    elif species.lower() == 'tiger':
        return 'Tiger Habitat'
    else:
        return 'Temporary Habitat'
        
class Hyena(Animal):
    species = 'Hyena'
    habitat = gen_zoo_habitats(species)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"
    
class Lion(Animal):
    species = 'Lion'
    habitat = gen_zoo_habitats(species)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

class Bear(Animal):
    species = 'Bear'
    habitat = gen_zoo_habitats(species)

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

class Tiger(Animal):
    species = 'Tiger'
    habitat = gen_zoo_habitats(species)

    def __init__(self, name):
        self.name = name    

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"

# assigns name based off species and selects a random name from list then removes that name from the list -- verify that works as intended
def gen_animal_name(species, name):
    if species.lower() == 'hyena':
        name = cleaner_names[random.randint(0, 10)]
        cleaner_names.remove(name)
    elif species.lower() == 'lion':
        name = cleaner_names[random.randint(11, 22)]
        cleaner_names.remove(name)
    elif species.lower() == 'bear':
        name = cleaner_names[random.randint(22, 31)]
        cleaner_names.remove(name)
    else:
        name = cleaner_names[random.randint(32, 41)]
        cleaner_names.remove(name)

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

