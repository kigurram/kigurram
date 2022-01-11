'''
Method Overriding:
Method overriding is an example of run time polymorphism.
In this, the specific implementation of the method that is already provided by the parent class is provided by the child class.
It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding.
In method overriding, inheritance always required as it is done between parent class(superclass) and child class(child class) methods.
'''

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a cat.my name is %s and age is %s'%(self.name, self.age))
    def sound(self):
        print('MEOW')

class Dog(Cat):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'I am a Dog.my name is %s and age is %s'%(self.name, self.age))
    def sound(self):
        print('BOW BOW')


dog_obj = Dog('Doggy', 3)
dog_obj.info()



