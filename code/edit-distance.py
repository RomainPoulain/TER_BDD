import sqlite3
import nltk
import sys

print(nltk.edit_distance('slawek'.lower(),'Sławek'.lower()))
print(nltk.edit_distance('slawek staworko','staworko slawek')) #8
print('slawek p. staworko, dr. hdr'.replace('.',' ').replace(',',' ').split()) #['slawek', 'p', 'staworko', 'dr', 'hdr']

print(nltk.jaccard_distance(set('slawek staworko'.split()), set('staworko slawek'.split()))) # 0.0 
 # {'slawek, 'staworko'}
 # {'staworko', 'slawek'}


print(set('slawek staworko'))
#print(nltk.jaccard_distance(set('slawek staworko'.split()), set('staworko slawek'.split()))) # 0.0 


sys.exit(1)






COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = '../data/small-authors.txt'
DB_FILE = '../bdd/databases.db'
db = sqlite3.connect(DB_FILE)
db.row_factory = sqlite3.Row
c = db.cursor()


names = []
birth_dates = []
death_dates = []
req = "select ID, NAME, BIRTH_DATE, DEATH_DATE from AUTHORS"
result = c.execute(req)
print(type(result))
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
for x in range(len(valeur)):
    if valeur[x] is None:
        continue
    for i in range(x + 1, len(valeur)):
        
        ed = nltk.edit_distance((valeur[x]), (valeur[i]))
        dico = {"titre": valeur[x], "titre_compare": valeur[i], "distance": ed, "x": x, "i": i}
        a = ((dico["titre"]), "&&", (dico["titre_compare"]), "&&", (dico["distance"]), (dico["x"]), (dico["i"]))

        if ((dico["distance"]) < 6 and dico["titre"] != ' None ') and dico["titre_compare"] != ' None ':
            a = print("la distance entre", dico["titre"], "et", dico["titre_compare"], "est egal a", dico["distance"],
                      "l'indice x est", dico["x"], "l'indice i est", dico["i"])

            ed2 = nltk.edit_distance(listee[dico["x"]], listee[dico["i"]])
            print("la distance par rapport au personal name entre", listee[dico["x"]], "et", listee[dico["i"]], "est",
                  ed2)

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
    ed = nltk.edit_distance(author1.lower(), author2.lower())
    for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
        j = json.loads(record['json'])
        if 'alternate_names' in j:
            for alt_name in j['alternate_names']:
                tab_alt_names = alt_name
                #for x in range(alt_names):
                #    for i in range(x + 1, alt_names):
                #        ed2 = nltk.edit_distance(x, i)
                     
    return ed/(abs(author1)+abs(author2))

for x in range(len(names)):
    for i in range(x + 1, len(names)):
        dist_name(names[x],names[i])
'''    
def dist_date(date1,date2):
    if date1 = None:
        return None
    if date1 = None:
        return None
    new_date1 = int(date1)
    new_date2 = int(date2)
    ed = nltk.edit_distance(new_date1, new_date2)
    return ed/(abs(new_date1)+abs(new_date2))
'''    
#def dist_author(author_id_1,author_id_2):
#    if dist_name(author_id_1,author_id_2) < 0.2:
#        if dist_date(date1,date2) 