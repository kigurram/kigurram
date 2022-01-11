from threading import *
from time import *

class my_thread():

    def prepare_tea(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print('Boil Milk and tea powder for 5 mins')
        sleep(5)
    def task2(self):
        print('Add sugar and boil for 3 mins')
        sleep(3)
    def task3(self):
        print('Filter and serve')
        print('Done')

obj = my_thread()
t1 = Thread(target=obj.prepare_tea())
t1.start()
