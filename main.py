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



def name_remover(species, name):
    if species.lower() == 'hyena':
        return hy_names.remove(name)
    elif species.lower() == 'lion':
        return li_names.remove(name)
    elif species.lower() == 'bear':
        return be_names.remove(name)
    elif species.lower() == 'tiger':
        return ti_names.remove(name)
    else:
        pass

    
def gen_birthday(age, season):
    # month of dec
    # spring = 'Mar'
    # summer = 'June'
    # fall = 'Sept'
    # winter = 'Dec'
    # make so first month of season is birth month, and birth year is age subtracted from current year 2022
    year = 2022 - age

    if season.lower() == 'spring':
        return f'Mar 8th, {year}'
    elif season.lower() == 'summer':
        return f'June 8th, {year}'
    elif season.lower() == 'fall':
        return f'Sept 8th, {year}'
    elif season.lower() == 'winter':
        return f'Dec 8th, {year}'
    else:
        pass

def gen_animal_ID():
    id = random.randint(0, 1000)
    return id

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

# f = open('arrivingAnimals.txt', 'r')

# animals = [line.strip().split(',') for line in f]

# f.close()

# animals = tuple(animals)
counter = 0

instanced_animals = []





class Animal:    


    def __init__(self, age=0, sex='Male', color='undetermined', weight='1oz', species='undetermined', season='winter', prev_location='zoo'):
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight
        self.id = gen_animal_ID()
        self.species = species
        self.habitat = gen_zoo_habitats(species)
        self.name = gen_animal_name(species)
        name_remover(self.species, self.name)
        # reason choosing winter as default season is because start of new year in US lands in Winter
        self.season = season
        self.birthday = gen_birthday(age, season)
        self.prev_location = prev_location

    
    def __str__(self):
        # have all info for each new created instance push to zoo pop txt file
        return f"ID: {self.id}; {self.name}; {self.age} year old; birthdate: {self.birthday}; {self.color}; {self.sex}; {self.weight}; from: {self.prev_location}; habitat: {self.habitat}; arrived Dec 8, 2022 \n"

with open('arrivingAnimals.txt', 'r') as f:
    lines = [line.strip().split(',') for line in f]

    for line in lines:
        prev_loc = line[1::4][1]
        color = line[2::4][0]
        age = int(line[0][0:2:1])
        sex = line[0][10:18].find('female')
        # sexx = line[0][10:18]
        if int(sex) == -1:
            sex = 'male'
        else:
            sex = 'female'
        season = line[1][9:]
        temp_species = line[0][16:]
        s = temp_species
        if s.endswith('hyena'):
            s = 'hyena'
            # print(s)
        elif s.endswith('lion'):
            s = 'lion'
            # print(s)
        elif s.endswith('tiger'):
            s = 'tiger'
            # print(s)
        else:
            s = 'bear'
            # print(s)
        species = s
        weight = int(line[3][0:4])
        instanced_animals.append(Animal(age, sex, color, weight, species, season, prev_loc))

counter = 1

with open('zooPopulation.txt', 'a') as f:
    for animal in instanced_animals:
        f.write(str(animal))


# ------------- below classes aren't in use any longer, had to just put everything into animal class -------------------------------

# class Hyena(Animal):
#     species = 'Hyena'
#     habitat = gen_zoo_habitats(species)

#     def __init__(self):
#         self.name = gen_animal_name(self.species)
#         hy_names.remove(self.name)
#         super().__init__()

#     def __str__(self):
#         return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"
    
# class Lion(Animal):
#     species = 'Lion'
#     habitat = gen_zoo_habitats(species)

#     def __init__(self):
#         self.name = gen_animal_name(self.species)
#         li_names.remove(self.name)
#         super().__init__()

#     def __str__(self):
#         return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    

# class Bear(Animal):
#     species = 'Bear'
#     habitat = gen_zoo_habitats(species)

#     def __init__(self):
#         self.name = gen_animal_name(self.species)
#         be_names.remove(self.name)
#         super().__init__()    
#     def __str__(self):
#         return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"    
        
# class Tiger(Animal):
#     species = 'Tiger'
#     habitat = gen_zoo_habitats(species)

#     def __init__(self):
#         self.name = gen_animal_name(self.species)
#         ti_names.remove(self.name)
#         super().__init__()    

#     def __str__(self):
#         return f"ID: {self.id} {self.name} is a {self.age} year old {self.species}. They belong to the habitat: {self.habitat}"


# new_bear = Bear()
# new_tiger = Tiger()
# new_lion = Lion()
# new_hyena = Hyena()

# print(new_bear)
# print(new_tiger)
# print(new_lion)
# print(new_hyena)

# print(cleaner_names)