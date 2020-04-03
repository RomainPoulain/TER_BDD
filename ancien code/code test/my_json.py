import json

my_json = '{"name": "Khau0304lid Muhu0323ammad u02bbAliu0304 al-Hu0323au0304jj",\
"personal_name": "Jacques", "last_modified": {"type": "/type/datetime", "value":\
"2008-08-20T17:57:09.66187"}, "key": "/authors/OL1000057A", "type": {"key":\
"/type/author"}, "revision": 2},{"name": "sdsdsdzzdzdfdfe", "personal_name":\
"Khau0304lid Muhu0323ammad u02bbAliu0304 al-Hu0323au0304jj", "last_modified": {"type":\
"/type/datetime", "value": "2008-08-20T17:57:09.66187"}, "key": "/authors/OL1000057A",\
"type": {"key": "/type/author"}, "revision": 2}'
JsonList = []
Stack = []
LastJsonEndIndex = 0
PassADot = False
for i in range(len(my_json)):
    if PassADot:
        PassADot = False
        continue
    if my_json[i] == "{":
        Stack.append(my_json[i])
    elif my_json[i] == "}":
        Stack.pop()
        if Stack == []:
            JsonList.append(my_json[LastJsonEndIndex:i+1])
            LastJsonEndIndex = i+2
            PassADot = True
    else:
        pass
#print(JsonList[1])


for j in range(len(JsonList)):
    content = JsonList[j]
    content_json = json.loads(content)
    print(content_json['name'])

