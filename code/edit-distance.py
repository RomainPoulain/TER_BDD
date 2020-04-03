import sqlite3
import nltk


DB_FILE = '../bdd/databases.db'
db = sqlite3.connect(DB_FILE)
c = db.cursor()


valeur = []
listee = []
req = "select * from AUTHORS"
result = c.execute(req)
print(type(result))
rows = c.fetchall()
for rowz in rows:
    listee.append((' {1} '.format(rowz[0], rowz[3], )))
for row in rows:
    valeur.append((' {1} '.format(row[0], row[1], )))

x = 0
liste = []
for x in range(len(valeur)):
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
