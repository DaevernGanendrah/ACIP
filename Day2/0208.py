#More on Lists
from collections import deque

data = [1,5,8,13,2,8,6,9,3]
print("Demo1:data=",data)

print("Demo2:first item with value 8 is at index",data.index(8))
print("Demo3:first item with value 8 after index 3 is at index",data.index(8,3))
print("Demo4:The are number of occurrence of 8 is",data.count(8))

data.sort(reverse=True)
print("Demo5:data=",data)

data.sort()
print("Demo6:data=",data)

data.reverse()
print("Demo7:data=",data)

data.clear()
print("Demo8:data=",data)

data.append(2)
data.insert(0,4)
print("Demo9:data=",data)

#Using List as Stack (FILO)
data.append(3)     #Similar to "push" in Stack
print("Demo10:data=",data)

item = data.pop()
print("Demo11:data=",data," item popped is",item)

#Using List as Queue (FIFO)
q = deque(data)
q.append(1)         #Similar to "enqueue"
item = q.popleft()  #Similar to "dequeue"
print("Demo11:q=",q," item enqueued is ",item)
