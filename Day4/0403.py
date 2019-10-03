'''
This function searches for first occurrence of RE pattern within the string,
with optional flags.
'''
import re
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
matchObj = re.match( r'.*dogs', line, re.M|re.I)
if matchObj:
    print ("match --> matchObj.group()\t:", matchObj.group())
else:
    print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
    print("search --> searchObj.group()\t:", searchObj.group())
else:
    print("Nothing found!!")
