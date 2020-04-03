import re,sqlite3
#with open("openlibrary2.py") as origin_file:
#    for line in origin_file:
#        line = re.findall(r'name', line)
#        if line:
#           line = line[0].split('"')[3]
#        print(line)

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS OPENLIBRARY3(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom TEXT,
     personal_name TEXT
)
""")
conn.commit()

test = []
test.append(("violette", "albert corbe"))
test.append(("test", "jose fonte"))
test.append(("Roger", "roger mila"))
test.append(("Mireille", "moussa sissoko"))
print(test)
cur.executemany("""
            INSERT INTO OPENLIBRARY3(nom,personal_name) VALUES(?,?)""", test)

OpenLibrary = []
name = []

print(test)

with open("openlibrary.json") as origin:
    for line in origin:
        if not "name" in line:
           #print('NULL')
           continue
        try:
            #print(line.split('"')[3])
            name.append(line.split('"')[3])
            OpenLibrary.append(("line.split('\"')[3]"))
        except IndexError:
            print



#print(name)
#print(OpenLibrary)
