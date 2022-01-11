def factorial(num):
    res = 1
    for i in range(num):
        res += i*res
    return res

print(factorial(4))

