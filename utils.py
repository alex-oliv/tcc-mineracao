import json

import json
  
f = open('result.json')
  
data = json.load(f)
  
for i in data:
    print(i)
  
f.close()