#Pyhton program to access the super class constructor from sub class
class Father():
    def __init__(self,property):
        self.property = property
    def display(self):
        print(f'Father"s Property:',self.property)

class son(Father):
    def __init__(self, son_prop, property):
        super().__init__(property)
        self.son_prop = son_prop
    def display(self):
        print(f'Father"s Property:%s\nSon"s Property:%s'%(self.property,self.son_prop))

s_obj = son(200, 300)
s_obj.display()