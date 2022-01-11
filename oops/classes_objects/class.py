#class is a collection of objects
#Object contains attributes and actions

class employee(object):
    #attributes mens variables
    name = 'Kiran'
    age = '36'
    sal = '20000'

    def display(self):
        print(self.name)
        print(self.age)
        print(self.sal)

class_obj = employee()
class_obj.display()