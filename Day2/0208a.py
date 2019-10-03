#Stack Example
def isWellFormed(s:str)->bool:
    sOpen = "{[("
    sClose= "}])"
    open = []
    for i in range(len(s)):
        if s[i] in sOpen:
            open.append(s[i]) #Push
        elif s[i] in sClose:
          if len(open)==0: return False
          b = open.pop()
          if sOpen.index(b)!=sClose.index(s[i]): return False
    return len(open)==0

def test(s:str)->None:
    print(s,("is not WellFormed","is WellFormed")[isWellFormed(s)])

test("[(1,2),(3,4)]") #WellFormed
test("[(1,2),(3,4),[(5,3),(4,6)],(8,4)]") #WellFormed
test("[(1,2),(3,4),[(5,3,(4,6)],(8,4)]") #Not WellFormed
test("[(1,2),{100:'Ali',200:'Abu'},[(5,3),(4,6)],(8,4)]") #WellFormed
test("[(1,2),(3,4)") #Not WellFormed
test("[(1,2),(]3,4)") #Not WellFormed