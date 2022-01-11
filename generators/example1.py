def func(x,y):
    while x<=y:
        yield x
        x+=1

res = func(5,10)
for i in res:
    print(i, end='')