# Creating a New Class from a existing class, so the new class will acquire all the features of the existing classes is called Inheritance
#Existing class is called as Super Class
#Inherited class is called as a base class

class bank(object):
    #to declare and intilise the variables
    def __init__(self):
        self.name = 'Kiran'
        self.acno = '36'
        self.balance = '20000'
        self.__loan_amount = '3000000'

    def bank_display(cls):
        print(cls.name)
        print(cls.acno)
        print(cls.balance)
        print(cls._bank__loan_amount) #name mangling is required to access private data

class branch(bank):
    def __init__(self):
        super().__init__()
        self.branch = 'Gachibowli'
    def display(cls):
        print(cls.balance)
        print(cls.branch)

branch_obj = branch()
branch_obj.display()