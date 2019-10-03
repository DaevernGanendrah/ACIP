import functools

data = [3,2,4,5,6,7,8,9,7,8]

largest = functools.reduce(lambda x,y: (y,x)[x>y], data)
print('The largest value is ',largest)

sum = functools.reduce(lambda x,y: x + y, data)
print('The total is ',sum)

