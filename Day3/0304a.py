#Arbitrary Argument Lists
def concat(*args, sep="/"):
    return sep.join(args)

def Min(min:int,*items)->int:
    for item in items:
        if type(item) is int:
            if min>item: min = item
    return min

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
print(Min(3,5,2,8,7,4,9,6))
print(Min(3,5,2,"Hello",8,7,4,9,6))
print(Min(3,5,4,9,6))
print(Min(3,5))
print(Min(5,3))
print(Min(5))
