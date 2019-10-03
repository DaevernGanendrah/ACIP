def isLeapYear(year:int)->bool:
    if (year%4)!=0: return False
    if (year%100)!=0: return True
    if (year%400)!=0: return False
    return True

def constructCalender(year:int):
    calender = []
    daysNumbers = [31,(28,29)[isLeapYear(year)], \
                   31,30,31,30,31,31,30,31,30,31]
    for m in range(12):
        calender.append([])
        for d in range(daysNumbers[m]): calender[m].append("D")
    return calender

def showCalender(cal)->None:
    monthNames = ["JAN","FEB","MAR","APR","MAY","JUN", \
                  "JUL","AUG","SEP","OCT","NOV","DEC"]
    for m in range(12):
        print(monthNames[m],end=":")
        for d in cal[m]:
            print(d,end="")
        print()

year = int(input("Year>>"))

cal = constructCalender(year)

showCalender(cal)
