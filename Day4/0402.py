'''
The re.match function returns a match object on success, None on failure. 
We use group(num) or groups() function of match object to get matched 
expression
'''
import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print ("matchObj.group()\t:",  matchObj.group())
    print ("matchObj.group(1)\t:", matchObj.group(1))
    print ("matchObj.group(2)\t:", matchObj.group(2))
else:
    print ("No match!!")