class student():
    def __init__(self, name, marks=0):
        self.name = name
        self.marks = marks
    def student_details(self):
        print(f'Student Name:%s\nStudent Marks:%s'%(self.name,self.marks))

stu_object = student('Pranav',100)
stu_object.student_details()