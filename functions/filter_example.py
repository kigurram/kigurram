def check_even(num):
    if num%2==0:
        return True
    else:
        return False

print(list(filter(check_even, [1,2,3,4,5])))