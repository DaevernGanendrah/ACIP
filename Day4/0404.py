'''
One of the most important re methods that use regular expressions is sub.

This method replaces all occurrences of the RE pattern in string with repl,
substituting all occurrences unless max is provided. This method returns
modified string.
'''
import re
phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print ("Phone Num : ", num)
