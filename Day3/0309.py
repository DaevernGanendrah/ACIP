data = [3,2,4,5,6,7,8,9,7,8]

#--- Methods #1 --------
evens = []

for i in range(len(data)):
    if (data[i]%2)==0:
        evens.append(data[i])

print(evens)

#--- Methods #2 --------
def isEven(x):
    return (x%2)==0

evens2 = list(filter(isEven, data))
print(evens2)


#--- Methods #3 --------
evens3 = list(filter(lambda x: (x % 2)==0, data))
print(evens3)



