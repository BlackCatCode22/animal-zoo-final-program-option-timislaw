class Animal:
    habitat = 'Zoo'
    def __init__(self, name, species, age, sex, color, weight):
        self.name = name
        self.species = species
        self.age = age
        self.sex = sex
        self.color = color
        self.weight = weight



bozoMonke = Animal('Bozo', 'Monkey', 45, 'Male', 'Black', '10 oz')
yoloMonke = Animal('Yolo', 'Monkey', 42, 'Female', 'Brown', '9 oz')

print(bozoMonke)
print(yoloMonke)

print(bozoMonke == yoloMonke)

