from threading import Thread

class my_thread_claass(Thread):
    def __init__(self, st):
        Thread.__init__(self)
        self.st = st

    def run(self):
        print(self.st)

t1 = my_thread_claass('Kiran')
t1.start()
t1.join()