# Class is an example of encapsulation

class employee(object):
    #to declare and intilise the variables
    def __init__(self):
        self.name = 'Kiran'
        self.age = '36'
        self.sal = '20000'

    def display(self):
        print(self.name)
        print(self.age)
        print(self.sal)

class_obj = employee()
class_obj.display()