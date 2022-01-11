#Python Program to use class method to handle the common feature of all the instances of bird class

class bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print('Bird %s can fly with %s Wings'%(name, cls.wings))


bird.fly('Flamingo')
bird.fly('Pigeon')



