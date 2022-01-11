#Filter will filter out the elements of a sequence depending on the result
lst = [10,9,8,7,6,5,4,3,2,1]
res = list(filter(lambda x: (True if x%2==0 else False), lst))
print(res)