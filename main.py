import random
from itertools import islice

f = open('animalNames.txt', 'r')

# make if/else that takes the lines and puts into a separate name list, hyena names, lion names, etc
names = [line.strip() for line in f]

f.close()
counter = 0

clean_names = []
cleaner_names = []

for line in names:
    if ' ' in line:
        clean_names.append(line)
            
for index in clean_names:
    if counter % 2 != 0  :
        cleaner_names.extend(word for word in index.split() if ',' in word)
    counter = counter + 1

counter = 0

# use strip method to clean up each available name 
cleaner_names = [s.strip(',') for s in cleaner_names]

# islicing -- https://docs.python.org/3/library/itertools.html#itertools.islice
length_to_split = [10, 11, 9, 9]

input = iter(cleaner_names)
cleaner_names = [list(islice(input, elem)) for elem in length_to_split]
# used islice to clean up lists into sub lists and then reassigned each sublist to a new name group
hy_names = cleaner_names[0]
li_names = cleaner_names[1]
be_names = cleaner_names[2]
ti_names = cleaner_names[3]

def gen_birthday():
    pass

def gen_animal_ID():
    id = random.randint(0, 1000)
    return id

class Animal:
# temporary habitat -- make so species determines which habitat is placed into; hyena habitat, lion habitat, etc
    
    def __init__(self, age=0, sex='Male', color='N/A', weight='1oz'):
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
        self.id = gen_animal_ID()

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
            
# assigns name based off species and selects a random name from list then removes that name from the list -- verify that works as intended
def gen_animal_name(species):
    if species.lower() == 'hyena':
        return random.choice(hy_names)
    elif species.lower() == 'lion':
        return random.choice(li_names)
    elif species.lower() == 'bear':
        return random.choice(be_names)
    else:
        return random.choice(ti_names)
    














f = open('arrivingAnimals.txt', 'r')

animals = [line.strip() for line in f]

f.close()

animals = tuple(animals)

# print(animals[15])


# try fifo linked list to organize data and make a species class out of each one


counter = 0

for animal in animals:
    counter = counter + 1
    # start organizing info into different classes
    if type(animal[counter]) == str:
        # print('admitted', counter)
        pass
    if animal.find('spring'):
        print('spring', counter)
    elif animal.find('winter'):
        print('winter', counter)
    elif animal.find('fall'):
        print('fall', counter)
    else:
        print('summer', counter)
    print(animal)



print(animals[0].find())
















class Hyena(Animal):
    species = 'Hyena'
    habitat = gen_zoo_habitats(species)

    def __init__(self):
        self.name = gen_animal_name(self.species)
        hy_names.remove(self.name)
        super().__init__()

    def __str__(self):
        return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"
    
class Lion(Animal):
    species = 'Lion'
    habitat = gen_zoo_habitats(species)

    def __init__(self):
        self.name = gen_animal_name(self.species)
        li_names.remove(self.name)
        super().__init__()

    def __str__(self):
        return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

class Bear(Animal):
    species = 'Bear'
    habitat = gen_zoo_habitats(species)

    def __init__(self):
        self.name = gen_animal_name(self.species)
        be_names.remove(self.name)
        super().__init__()    
    def __str__(self):
        return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    
        
class Tiger(Animal):
    species = 'Tiger'
    habitat = gen_zoo_habitats(species)

    def __init__(self):
        self.name = gen_animal_name(self.species)
        ti_names.remove(self.name)
        super().__init__()    

    def __str__(self):
        return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"


new_bear = Bear()
new_tiger = Tiger()
new_lion = Lion()
new_hyena = Hyena()

# print(new_bear)
# print(new_tiger)
# print(new_lion)
# print(new_hyena)

# print(cleaner_names)