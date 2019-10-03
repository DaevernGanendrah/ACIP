#List Comprehensions
list1 = []
for x in range(10):
    list1.append(x**2)
print(list1)

list2 = [x**2 for x in range(10)]
print(list2)


grid1=[]
for r in range(3):
    grid1.append([])
    for c in range(2):
        grid1[r].append(0.0)
print(grid1)

grid2 = [[0.0 for c in range(2)] for r in range(3)]
print(grid2)

tuples1 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            tuples1.append((x, y))
print(tuples1)

tuples2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(tuples2)
