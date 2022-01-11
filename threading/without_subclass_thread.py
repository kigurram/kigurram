from threading import *

class my_thread():

    def __init__(self, st):
        self.st = st

    def display(self, x,y,z):
        print('args:',x,y,z)
        

thread_obj = my_thread('Kiran')
t1= Thread(target=thread_obj.display, args=(1,2,3))
t1.start()

