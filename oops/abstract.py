# Abstract is hiding a variable outside the class
#Accesing some part of data which is abstract is called mangling

class bank(object):
    #to declare and intilise the variables
    def __init__(self):
        self.name = 'Kiran'
        self.acno = '36'
        self.balance = '20000'
        self.__loan_amount = '3000000'

    def display(self):
        print(self.name)
        print(self.acno)
        print(self.balance)
        print(self._bank__loan_amount) #name mangling is required to access private data

class_obj = bank()
class_obj.display()