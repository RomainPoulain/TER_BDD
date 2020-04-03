import json
import requests
import sqlite3, nltk
file = open('newjson.json', 'r')
content = file.read()
file.close()
#print(content)
#print(content)
#content_json = json.loads(content)
#print(content_json['revision'])
#Afficher un tableau simple (liste)
#print type(content_json)
#print(content_json['properties']['wikipedia']['description'])
#Afficher un tableau contenant des cles et valeurs
#Modification de la valeur
#print content_json['title']
#content_json['title'] = 'nouvelle valeur'
#suppression d'une ligne
#del content_json['title']
#print content_json
#Connection a une base de donnees

#connection = sqlite3.connect('base.db')
#cursor = connection.cursor()
#print sqlite3.version
#Creation table
#table = """ CREATE TABLE IF NOT EXISTS Visiteurs (
#                    id integer PRIMARY KEY,
#                   nom text NOT NULL,
##                    age integer
#                    ); """
#cursor.execute(table)
#connection.commit()
#Insertion dans la table de donnees
#insertion = cursor.execute("""insert into 'Visiteurs'(id,nom,age) values(1,'coumba',30)""")
#insertion = cursor.execute("""insert into 'Visiteurs'(id,nom,age) values(2,'coco',30)""")
#print("Record inserted successfully  ", cursor.rowcount)
#connection.commit()
#Recuperer les donnees e
#sqlite_select_query = """SELECT * from Visiteurs"""
#cursor.execute(sqlite_select_query)
#response = cursor.fetchall()
#connection.commit()
#print len(response)
#print response
#Recuperer des donnees d'un site
#Utilisation d'une bibliotheque 'requests'

revision = ["1","2","3"]
name = ["olivier","jean","jacques"]


conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS film(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     titre TEXT,
     date date
)
""")
conn.commit()

film = []
film.append(("violette", "2018-05-23"))
film.append(("violete", "2018-05-23"))
film.append(("Alice au pays des merveilles", "2017-12-23"))
film.append(("Alice aux pays des merveilles", "2017-12-23"))
film.append(("La plaete des singes ", "2015-02-1"))
film.append(("La planete des singes 2", "2016-03-16"))
film.append(("Titanic", "2012-02-02"))
film.append(("King Kong", "2004-04-12"))
film.append(("Kink Konk", "2005-09-25"))
film.append(("La vie", "2009-10-15"))
film.append(("L'histoire d'un homme", "2002-04-15"))
film.append(("L'histoire du temps", "2018-11-30"))
film.append(("Une fois mais pas deux", "2009-11-15"))
film.append(("Pourquoi pas", "2012-12-19"))
film.append(("Le destin d'une vie", "2011-09-29"))
film.append(("L'enfer ou le paradis", "2001-09-12"))
film.append(("Les chats", "2005-06-15"))
film.append(("Les chiens", "2010-07-12"))
film.append(("Les serpents", "2007-07-17"))
film.append(("Ling kong", "2012-12-12"))
film.append(("Les chienss", "2018-06-23"))
#print(film)
cur.executemany("""
INSERT INTO film(titre, date) VALUES(?, ?)""", film)

y = 0

valeur = []
valdate = []
req = "select * from film"
result = cur.execute(req)
print(type(result))
for row in result:
	#print(row[1])
	#print(row[2])
	valeur.append(row[1])
	valdate.append(row[2])


#def parcours():
	for i in range(0,len(valeur)-1):
	#ed = nltk.edit_distance(valeur[0], valeur[i])
	#ed = nltk.edit_distance(valeur[i], valeur[i+1])
	#print(valeur[i], ed)
	#print(valeur[i+1], ed
	  ed = nltk.edit_distance(valeur[0], valeur[i + 1])
	  #print(valeur[i], ed)
	  i = i + 1
#if (valeur[i] == "Les chienss"):
	#y = y + 1
	#while y!=24:
		#parcours()
#for j in range(0,len(valdate)-1):
	#ed = nltk.edit_distance(valdate[0], valdate[j])
	#ed = nltk.edit_distance(valdate[j], valdate[j+1])
	#print(valdate[j], ed)
	#j = j + 1

print(valeur)
print(valdate)