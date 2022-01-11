from threading import *

def disdplay(name):
    print('Hi Good Morning:%s'%name)

for i in range(5):
    t = Thread(target=disdplay, args=('Kiran',))
    t.start()



