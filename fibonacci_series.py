def fibonacci():
    f1=0
    f2=1
    print(f1)
    print(f2)
    for i in range(1,10):
        f=f1+f2
        print(f)
        f1,f2 = f2, f

fibonacci()