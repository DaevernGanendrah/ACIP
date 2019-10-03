ns = []
while True: #Busy loop
    s = input("Number>>").strip()
    if len(s)==0: break
    ns.append(int(s)) #Assume s is well-fomed int
    
if len(ns)>0:
    max = ns[0]
    total = 0;
    for n in ns:
        if n>max: max = n
        total += n
    print("Total:",total)
    print("Average:",total/len(ns))
    print("Max:",max)
