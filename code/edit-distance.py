import sqlite3
import nltk
import sys
import csv
import json

'''
print(nltk.edit_distance('slawek'.lower(),'Sławek'.lower()))
print(nltk.edit_distance('slawek staworko','staworko slawek')) #8
print('slawek p. staworko, dr. hdr'.replace('.',' ').replace(',',' ').split()) #['slawek', 'p', 'staworko', 'dr', 'hdr']

print(nltk.jaccard_distance(set('slawek staworko'.split()), set('staworko slawek'.split()))) # 0.0 
 # {'slawek, 'staworko'}
 # {'staworko', 'slawek'}


print(set('slawek staworko'))
#print(nltk.jaccard_distance(set('slawek staworko'.split()), set('staworko slawek'.split()))) # 0.0 


sys.exit(1)

'''




COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = 'small-authors.txt'
DB_FILE = 'databases.db'
db = sqlite3.connect(DB_FILE)
db.row_factory = sqlite3.Row
c = db.cursor()


names = []
birth_dates = []
death_dates = []
req = "select ID, NAME, BIRTH_DATE, DEATH_DATE from AUTHORS"
result = c.execute(req)
rows = c.fetchall()
for rowz in rows:
    birth_dates.append((' {1} '.format(rowz['ID'], rowz['BIRTH_DATE'], )))
for row in rows:
    names.append((' {1} '.format(row['ID'], row['NAME'], )))
for rowz in rows:
    death_dates.append((' {1} '.format(rowz['ID'], rowz['DEATH_DATE'], )))
'''
x = 0
liste = []
for x in range(len(names)):
    if names[x] is None:
        continue
    for i in range(x + 1, len(names)):
        
        ed = nltk.edit_distance((names[x]), (names[i]))
        dico = {"titre": names[x], "titre_compare": names[i], "distance": ed, "x": x, "i": i}
        a = ((dico["titre"]), "&&", (dico["titre_compare"]), "&&", (dico["distance"]), (dico["x"]), (dico["i"]))

        if ((dico["distance"]) < 6 and dico["titre"] != ' None ') and dico["titre_compare"] != ' None ':
            a = print("la distance entre", dico["titre"], "et", dico["titre_compare"], "est egal a", dico["distance"],
                      "l'indice x est", dico["x"], "l'indice i est", dico["i"])

            #ed2 = nltk.edit_distance(listee[dico["x"]], listee[dico["i"]])
            #print("la distance par rapport au personal name entre", listee[dico["x"]], "et", listee[dico["i"]], "est",
            #      ed2)

# Jaccard distance





for x in range(len(valeur)):
    for i in range(x + 1, len(valeur)):
        ed = nltk.jaccard_distance(set(valeur[x]), set(valeur[i]))
        dico = {"titre": valeur[x], "titre_compare": valeur[i], "distance": ed, "x": x, "i": i}
        a = (
        (dico["titre"]), "&&", (dico["titre_compare"]), "&&", (dico["distance"]), "&&", (dico["x"]), "&&", (dico["i"]))

        if ((dico["distance"]) < 0.32 and dico["titre"] != ' None ') and dico["titre_compare"] != ' None ':
            a = print("la distance entre", dico["titre"], "et", dico["titre_compare"], "est egal a", dico["distance"],
                      "et l'indice x est :", dico["x"], "et l'indice i est :", dico["i"])

            ed2 = nltk.jaccard_distance(set(listee[dico["x"]]), set(listee[dico["i"]]))
            print("la distance par rapport au personal name entre", listee[dico["x"]], "et", listee[dico["i"]], "est",
                  ed2)
'''








tab_alt_names = []
def dist_name(author1,author2):
    ed = nltk.edit_distance(author1, author2)
    for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
        j = json.loads(record['json'])
        #Voir comment faire avec les alternatives_names
        #if 'alternate_names' in j:
        #    for alt_names in j['alternate_names']:
        #        tab_alt_names.append(nltk.edit_distance(alt_names,author1))
        #        alt_names_min = min(tab_alt_names)
        #        print(alt_names_min)

                #print(alt_name)
                #tab_alt_names = alt_name

                #for x in range(alt_names):
                #    for i in range(x + 1, alt_names):
                #        ed2 = nltk.edit_distance(x, i)
    return ed/(abs(len(author1))+abs(len(author2)))

def dist_date(author1,author2):
    date1 = ""
    date2 = ""
    result = ""
    for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
        j = json.loads(record['json'])
        if 'birth_date' in j:
            #print(j['birth_date'], j['name'])
            tuple = (j['birth_date'],j['name'])
            birth_date,author = tuple
            #MEME CHOSE AVEC DEATH_DATE
            #On veut faire en sorte que la date corresponde à l'auteur du parametre
            #if l'author est egal à celui dans le parametre author1
            date1 = birth_date
            # if l'author est egal à celui dans le parametre author2
            date2 = birth_date
        if 'birth_date' in j and author1 == j['name']:
            date1 = j['birth_date']
        if 'birth_date' in j and author2 == j['name']:
            date2 =j['birth_date']
    if date1 == None:
        return None
    if date1 == None:
        return None
    #Convertir en in
    #new_date1 = int(date1)
    #new_date2 = int(date2)
    ed = nltk.edit_distance(date1, date2)
    try:
        result = ed/(abs(len(date1))+abs(len(date2)))
    except: ZeroDivisionError
    return result







valeur = []
valeur2 = []
'''
for x in range(len(names)):
    print("Looping x=%d" % x)
    for i in range(x + 1, len(names)):
        print("Looping i=%d" % i)
        if dist_name(names[x],names[i]) < 0.3 and dist_name(names[x],names[i])!=None:
            print("If condition was true")
            print(dist_date(names[x],names[i]))
        else:
            print("If condition was false")
'''
for x in range(len(names)):
    for i in range(x + 1, len(names)):
        if dist_name(names[x],names[i]) < 0.3 and dist_name(names[x],names[i])!=None:
            print(dist_date(names[x],names[i]))
#for z in zip(valeur,valeur2):



def dist_author(author_id_1,author_id_2):
    if dist_name(author_id_1,author_id_2) < 0.2:
        if dist_date(author_id_1,author_id_2) < 0.2:
            print("SIMILAIRE")
        else:
            print("Name similaire pas date")
    if dist_name(author_id_1,author_id_2) >0.6:
        print("Name different")
    if dist_date(author_id_1, author_id_2) >0.6:
        print("Date differente")