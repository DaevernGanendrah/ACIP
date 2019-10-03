#Using range function
print("\n\nDemo1",end=':')
for i in range(10): print(i,end=' ')

print("\n\nDemo2",end=':')
for i in range(0,10,1): print(i,end=' ')

print("\n\nDemo3",end=':')
for i in range(3,10): print(i,end=' ')

print("\n\nDemo4",end=':')
for i in range(3,10,2): print(i,end=' ')

print("\n\nDemo5",end=':')
for i in range(10,0,-1): print(i,end=' ')

print("\n\nDemo6",end=':')
for i in range(-10,-20,-3): print(i,end=' ')

#Using Tuple
print("\n\nDemo7",end=':')
for i in (5,7,2,-4,1): print(i,end=' ')

#Using List
print("\n\nDemo8",end=':')
for i in [5,7,2,-4,1]: print(i,end=' ')

print("\n\nDemo9",end=':\n')
for i,v in enumerate(['Nenas','Ciku','Durian','Pisang']):
    print("\t",i,':',v)

#Using Dictionary
print("\n\nDemo10",end=':\n')
students = {1000:"Ali", 1001:"Abu", 1004:"Azizi", 1006:"Ahmad"}
for k, v in students.items(): print("\t",k,':',v)

#To loop over two or more sequences at the same time
print("\n\nDemo11",end=':\n')
keys = [1000, 1001, 1004, 1006]
names =['Ali', 'Abu', "Azizi", "Ahmad"]
for k, v in zip(keys,names): print("\t",k,':',v)

#Reorder the list items
print("\n\nDemo12",end=':\n')
fruits = ['Apple', 'Orange', 'Apple', 'Pear', 'Orange', 'Banana']
for f in sorted(fruits): print("\t",f)

#Reorder and elimanate redundance list items
print("\n\nDemo13",end=':\n')
for f in sorted(set(fruits)): print("\t",f)
