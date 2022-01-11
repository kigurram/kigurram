# A python program to understand class variable or static variable
class example():
    x = 10

    #This is Class Method decorator
    @classmethod
    def modify(cls):
        cls.x += 1

ex = example()
ex1 = example()

print('x in ex=',ex.x)
print('x in ex1=',ex1.x)

ex.modify()
print('x in ex=',ex.x)
print('x in ex1=',ex1.x)


