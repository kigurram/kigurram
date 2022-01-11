class student():
    def __init__(self):
        self.name = 'Pranav'
        self.classname = '1H'
        self.rollnum = '301012'
    def student_details(self):
        print(f'Student Name:%s\nStudent ClassName:%s\nStudent Roll Number:%s'%(self.name,self.classname,self.rollnum))

stu_object = student()
stu_object.student_details()