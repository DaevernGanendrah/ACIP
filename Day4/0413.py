class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [D, C, B]:
    try:
        raise cls()
    except D:
        print("D")
    #except C:
        #print("C")
    #except B:
        #print("B")
    finally:
        print("Finally block")
