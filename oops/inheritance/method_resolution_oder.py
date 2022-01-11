#Python Program to understand the order of execution of methods in several base classes according to MRO

class A(object):
    def method(self):
        print('A Class Method')
class B(object):
    def method(self):
        print('B Class Method')
class C(object):
    def method(self):
        print('C Class Method')
class X(A, B):
    def method(self):
        print('X Class Method')
        super().method()
class Y(B, C):
    def method(self):
        print('Y Class Method')
        super().method()
class P(X,Y,C):
    def method(self):
        print('P Class Method')
        super().method()
P= P()
P.method()