#Recursion

def Fact(n)->int:
    assert isinstance(n, int)
    assert n>=0

    if (n<2):
        return 1
    else:
        return Fact(n-1) * n


for i in range(13):
    print("Fact({})\t:{}".format(i,Fact(i)))



