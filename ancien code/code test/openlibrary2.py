import json

file = open('openlibrary3.json', 'r')
content = file.read()
#file.close()
content_json = json.loads(content)
print(content_json['nom']['name'])
name = []
#
nom = "nom"
#nom = nom + str(i)

for i in range(10):
    nom = nom + str(1)
    a = content_json['nom1']['personal_name']
    name.append(a)
    i = i + 1
    print(nom)
print(name)