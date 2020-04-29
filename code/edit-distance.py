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







DB_FILE = '../bdd/databases.db'
db = sqlite3.connect(DB_FILE)
db.row_factory = sqlite3.Row
c = db.cursor()


valeur = []
listee = []
req = "select ID, NAME, PERSONAL_NAME from AUTHORS"
result = c.execute(req)
print(type(result))
rows = c.fetchall()
for rowz in rows:
    listee.append((' {1} '.format(rowz['ID'], rowz['PERSONAL_NAME'], )))
for row in rows:
    valeur.append((' {1} '.format(row['ID'], row['NAME'], )))

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
