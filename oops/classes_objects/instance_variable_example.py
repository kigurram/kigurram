# A python program to understand instance variable
class example():
    #this is a contructor
    def __init__(self):
        self.x = 10

    #Thi is InstanceMethod
    def modify(self):
        self.x += 1

ex = example()
ex1 = example()

print('x in ex=',ex.x)
print('x in ex1=',ex1.x)

ex.modify()
print('x in ex=',ex.x)
print('x in ex1=',ex1.x)


