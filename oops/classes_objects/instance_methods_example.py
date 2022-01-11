#Python programme using a student class with instance mmethods to process the data of several students

class student():
    def __init__(self, name='', marks=0):
        self.name = name
        self.marks = marks
    def display(self):
        print(f'Student Name:%s\nStudent Marks%s'%(self.name,self.marks))

    #Calculate Grades based on Marks
    def calulate_grade(self):
        if self.marks>=600:
            print(f'%s got first grade'%self.name)
        elif self.marks>=500:
            print(f'%s got Second grade' % self.name)
        elif self.marks>=350:
            print(f'%s got Third grade' % self.name)
        else:
            print(f'%s got Failed' % self.name)

#Create instance with some data from keyboard
n = int(input('Enter the Students Count'))
i=0
while i<=n:
    name = str(input('Enter Student Name'))
    marks = int(input('Enter Student Marks'))
    st_obj = student(name,marks)
    st_obj.display()
    st_obj.calulate_grade()
    i+=1