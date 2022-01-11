#Python program to create another version of DOB class within the person class

class Person():
    def __init__(self):
        self.name = 'Kiran'
        self.age = 36
    def display(self):
        print(f'Person Name:%s\nPerson Age:%s'%(self.name,self.age))

    class DOB():
        def __init__(self):
            self.dd = 8
            self.mm = 10
            self.yyyy = 1985
        def display(self):
            print(f'Person DOB: %s-%s-%s'%(self.dd, self.mm,self.yyyy))

p = Person()
p.display()
x= Person.DOB()
x.display()

