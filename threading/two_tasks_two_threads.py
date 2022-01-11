from threading import *
from time import *

class my_thread():
    def __init__(self,st):
        self.st = st
        self.l = Lock()
    def repeat(self):
        self.l.acquire()
        for i in range(1,6):
            print(self.st+':'+str(i))
            sleep(1)
        self.l.release()

obj1 = my_thread('Issue tickets ')
obj2 = my_thread('start show')

t1 = Thread(target=obj1.repeat)
sleep(0.1)
t2 = Thread(target=obj2.repeat)

t1.start()
t2.start()
