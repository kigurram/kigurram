import pickle
class emp(object):
    def __init__(self, emp_id, emp_name, emp_sal):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_sal = emp_sal
    def display(self):
        print(f"%s %s %s" %(self.emp_id,self.emp_name,self.emp_sal))

employee = emp('50665','KG','1900000')
employee.display()
file_obj = open('D:\kiran_python\\txt.txt', 'wb')
pickle.dump(employee, file_obj)
file_obj.close()
file_obj = open('D:\kiran_python\\txt.txt', 'rb')
p_obj = pickle.load(file_obj)
p_obj.display()










