#Python program to createa static method that counts the number of instances created for a class

class my_class:
    #this a class variable or static variable
    n=0

    def __init__(self):
        my_class.n+=1

    @staticmethod
    def display():
        print('No of Instances Created ',my_class.n)

cl1 = my_class()
cl3 = my_class()
my_class.display()
