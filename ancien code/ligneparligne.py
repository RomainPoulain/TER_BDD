import json, sqlite3, nltk, re
from json import JSONDecodeError

ligne = []
personal_nom = []
tout = []
last_modified = []
bio = []
key = []
birth_date = []
revision = []
type = []

conn = sqlite3.connect('database.db')
cur = conn.cursor()
#cur.execute(""" DROP TABLE OPENLIBRARY4""")
cur.execute("""
CREATE TABLE IF NOT EXISTS OPENLIBRARY4(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     personal_name TEXT,
     last_modified TEXT,
     key TEXT,
     birth_date INTEGER,
     revision INTEGER,
     type TEXT
)
""")
conn.commit()




with open('openlibrarytest.json') as file:
    for line in range(100):
        try:
            line = file.readline()
            content_json = json.loads(line)
        except JSONDecodeError:
            continue
        if not "name" in line:
            # print('NULL')
            ligne.append("NULL")
            continue
        try:
            # print(content_json['name'])
            ligne.append(content_json['name'])
        except IndexError:
            print
        if not "personal_name" in line:
            # print('NULL')
            personal_nom.append("NULL")
            continue
        try:
            # print(content_json['name'])
            personal_nom.append(content_json['personal_name'])
        except IndexError:
            print
        if not "last_modified" in line:
            last_modified.append("NULL")
            continue
        try:
            last_modified.append(content_json['last_modified']['value'])
        except IndexError:
            print
        if not "key" in line:
            key.append("NULL")
            continue
        try:
            key.append(content_json['key'])
        except IndexError:
            print
        if not "birth_date" in line:
            birth_date.append("NULL")
            continue
        try:
            birth_date.append(content_json['birth_date'])
        except IndexError:
            print
            if not "revision" in line:
                revision.append("NULL")
                continue
            try:
                revision.append(content_json['revision'])
            except IndexError:
                print
            if not "type" in line:
                type.append("NULL")
                continue
            try:
                type.append(content_json['type'])
            except IndexError:
                print
            """
            if not "bio\"" in line:
                # bio.append("NULL")
                continue
            try:
                # print(content_json['name'])
                bio.append(line)
            except IndexError:
                print
            """

resultat_name = []
for name in zip(ligne):
    resultat_name.append((name))
print(resultat_name)

print(" ")
print(" PERSONAL NAME")

resultat_personal_name = []
for personal_name in zip(personal_nom):
    resultat_personal_name.append((personal_name))
print(resultat_personal_name)

print(" ")
print(" KEY ")

resultat_key = []
for k in zip(key):
    resultat_key.append((k))
print(resultat_key)

print(" ")
print(" TYPE ")

resultat_type = []
for t in zip(type):
    resultat_type.append((t))
print(resultat_type)

resultat_last_modified = []
for l in zip(last_modified):
    resultat_last_modified.append((l))

resultat_birth_date = []
for b in zip(birth_date):
    resultat_birth_date.append((b))

print(" ")
print(" LAST MODIFIED ")

print(resultat_last_modified)

print(" ")
print(" BIRTH DATE")

print(resultat_birth_date)

print(" REVISION ")
print(" ")

print(revision)

cur.executemany("""
INSERT INTO OPENLIBRARY4(name) VALUES(?)""", resultat_name)
cur.executemany("""
INSERT INTO OPENLIBRARY4(personal_name) VALUES(?)""", resultat_personal_name)
cur.executemany("""
INSERT INTO OPENLIBRARY4(last_modified) VALUES(?)""", resultat_last_modified)
cur.executemany("""
INSERT INTO OPENLIBRARY4(key) VALUES(?)""", resultat_key)
cur.executemany("""
INSERT INTO OPENLIBRARY4(birth_date) VALUES(?)""", resultat_birth_date)
#cur.executemany("""
#INSERT INTO OPENLIBRARY4(revision) VALUES(?)""", revision)
cur.executemany("""
INSERT INTO OPENLIBRARY4(type) VALUES(?)""", resultat_type)



valeur = []

req = "select * from OPENLIBRARY4"
result = cur.execute(req)
#print(type(result))
for row in result:
    valeur.append(row[1])

#print(valeur)
"""
double = 0
liste = []

for x in range(len(valeur)):
    for i in range(x + 1, len(valeur)):
        ed = nltk.edit_distance(valeur[x], valeur[i])
        dico = {"titre": valeur[x], "titre_compare": valeur[i], "distance": ed}
        (dico["titre"], "&&", (dico["titre_compare"]), "&&", (dico["distance"]))
        double = dico["distance"] + dico["distance"]
    if double < 5:
        print(dico["titre"], "&&", (dico["titre_compare"]), "&&", (double))
"""