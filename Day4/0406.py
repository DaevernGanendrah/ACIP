import math
print('{} teach {}"'.format('Ali', 'Abu'))

print('{1} teach {0}"'.format('Ali', 'Abu'))

print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents)) #!r =''
print('The value of PI is approximately {0:.3f}.'.format(math.pi)) #.3f = 3 decimal points

print(" x x**2 x**3")
for x in range(1, 11):
    print(' {0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3)) #2d = spacing

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
print()
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

