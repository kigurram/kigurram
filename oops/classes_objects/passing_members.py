#A pyhton program to create EMP class and make all the members of the EMP class vailable to another class

class EMP:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self):
        print(f'Employee ID:%s\nEMployee Name:%s\nEmployee Salary:%s'%(self.id,self.name,self.salary))

#this class displays employee details
class My_class():
    #method to recieve employee instance
    #and display employee details
    def mymethod(EMP):
        #increment salary by 1000
        EMP.salary += 1000
        EMP.display()

emp_obj = EMP(1,'Kiran', 1000)
My_class.mymethod(emp_obj)




