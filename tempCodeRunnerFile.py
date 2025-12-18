from functools import reduce
l = [5,10,15]
sum = reduce(lambda x,y:x+y,l)
print(sum)
