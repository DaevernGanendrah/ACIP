#Queue Example
from collections import deque

def menu()->None:
    print("="*20)
    print(" A:Add new Item")
    print(" R:Remove First Item")
    print(" L:List Items")
    print(" X:Exit")
    print("="*20)

entries = deque([])

def Add()->None:
    global entries
    s = input("New Input>>").strip()
    entries.append(s)


while True:
    menu()
    s = input("Command>>").strip().upper()
    if s=="X": break
    if s=="A":
        Add()
    elif s=="R":
        if len(entries)==0:
            print("Nothing to remove!")
        else:
            print("Removed item",entries.popleft())
    elif s=="L":
        print("Items",end=':')
        print(list(entries))
        print()
    else:
        print("Invalid Command:",s)
print("Bye...")