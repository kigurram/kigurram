def check_prime(num):
    x=1
    for i in range(2, num):
        if num%i==0:
            x=0
            break
        else:
            x=1
    if x==1:
        print(str(num)+' is a PRIME')
    elif x==0:
        print(str(num) + ' is not a PRIME')
i=1
while i<=100:
    print(check_prime(i))
    i = i+1
