#with open('authorschema.json') as file:
 #   for i in range(10):
  #      line = file.readline()
   #     print(line)

import json

file = open('authorschema.json', 'r')
content = file.read()
file.close()
content_json = json.loads(content)
print(content_json['properties']['wikipedia']['description'])