# Condition of occurrence in different forms (or) Object/Method performing different behavior in different contexts

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a cat.my name is %s and age is %s'%(self.name, self.age))
    def sound(self):
        print('MEOW')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a Dog.my name is %s and age is %s'%(self.name, self.age))
    def sound(self):
        print('BOW BOW')

cat_obj = Cat('Kitty', 2)
dog_obj = Dog('Doggy', 3)

for animal in [cat_obj, dog_obj]:
    animal.sound()
    animal.info()
    animal.sound()



