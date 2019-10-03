def FruitShop(discount,**fruitsInfo):
    for k,v in fruitsInfo.items():
        print("Name:",k,"\tPrice:$",v)
    #for fruit in fruitsInfo:
    #    print(fruit,":",fruitsInfo[fruit])
    print("The discount is ", discount)


FruitShop(0.15,Apple=2.5,Durian=120,Rambutan=1.8)
#FruitShop(0.15,Apple=2.5,PisangEmas=1.1,Rambutan=1.8,Nenas=3.3)