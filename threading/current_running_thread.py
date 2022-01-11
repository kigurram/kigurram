import threading

#Finding the name of the present thread
print('Currently Running thread: %s'%threading.currentThread().getName())

if threading.currentThread() == threading.main_thread():
    print('Main thread')
else:
    print('Not a main thread')

