import json  #JavaScript Object Notation

data = {100:"Ali",101:"Abu",103:"Ahmad"}

s = json.dumps(data)
print(s)

f = open("data.json",'w')
json.dump(data,f)
f.close()

