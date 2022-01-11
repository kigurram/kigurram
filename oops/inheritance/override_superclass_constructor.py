#Pyhton program to access the base class constructor from sub class
class Father():
    def __init__(self):
        self.property = 80000000
    def display(self):
        print(f'Father"s Property:',self.property)

class son(Father):
    def __init__(self):
        self.property = 520000000
    def display(self):
        print(f'Fathers Property:', self.property)

s_obj = son()
s_obj.display()