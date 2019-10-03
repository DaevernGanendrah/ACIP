def Abbreviation(s:str)->str:
    s = s.strip()
    result = ""
    for w in s.split(" "):
        if len(w)>0:
            c = w[0]
            if c.isupper():
                result += c
    return result

print(Abbreviation("Information Technology"))
print(Abbreviation("   Visual   Basic   for   Application    "))
print(Abbreviation("Integreted Development Environment"))







