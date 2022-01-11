from threading import Thread

class my_thread_claass(Thread):

    def run(self):
        for i in range(6):
            print(i)

t1 = my_thread_claass()
t1.start()
t1.join()

