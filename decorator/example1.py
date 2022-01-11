
def decort(func):
    def inner_func(*args):
        value = func(*args)
        print('args:{}'.format(args))
        return 'Success'
    return inner_func

@decort
def sum(a,b):
    return a+b

print(sum(1,2))


