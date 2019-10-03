fruits = []
while True: #Busy loop
    fruit = input("Fruit>>").strip()
    if len(fruit)==0: break
    fruits.append(fruit)

#if "Pisang" in fruits: 
#    fruits.remove("Pisang") # Remove first Pisang
    
#while "Pisang" in fruits: 
#    fruits.remove("Pisang") # Remove all Pisang


#The following will remove all kind of Pisang including different cases
n = len(fruits)
for idx in range(n):
    if "PISANG" in fruits[n-idx-1].upper():
        del fruits[n-idx-1]

fruits.insert(0,"Kiwi Fruit")

for fruit in fruits: print(fruit)

