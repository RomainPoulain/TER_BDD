import sqlite3
import nltk
import sys
import csv
import json
from datetime import date, datetime
from math import exp


COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = 'small-authors.txt'
DB_FILE = '../bdd/databases.db'
db = sqlite3.connect(DB_FILE)
db.row_factory = sqlite3.Row
c = db.cursor()

names = []
birth_dates = []
death_dates = []
tab_id = []
req = "select ID, NAME, BIRTH_DATE, DEATH_DATE from AUTHORS"
result = c.execute(req)
rows = c.fetchall()
for rowz in rows:
    tab_id.append((' {0} '.format(rowz['ID'], )))
for rowz in rows:
    birth_dates.append((' {1} '.format(rowz['ID'], rowz['BIRTH_DATE'], )))
for row in rows:
    names.append((' {1} '.format(row['ID'], row['NAME'], )))
for rowz in rows:
    death_dates.append((' {1} '.format(rowz['ID'], rowz['DEATH_DATE'], )))

tab_id2 = []
req2 = "select ID from AUTHORS"
result = c.execute(req)
for i in range(0, 1000):
    try:
        tab_id2.append(c.fetchone()['ID'])
    except TypeError:
        None


# '''  VERSION AVEC LES DICTIONNAIRES
# x = 0
# liste = []
# for x in range(len(names)):
#     if names[x] is None:
#         continue
#     for i in range(x + 1, len(names)):

#         ed = nltk.edit_distance((names[x]), (names[i]))
#         dico = {"titre": names[x], "titre_compare": names[i], "distance": ed, "x": x, "i": i}
#         a = ((dico["titre"]), "&&", (dico["titre_compare"]), "&&", (dico["distance"]), (dico["x"]), (dico["i"]))

#         if ((dico["distance"]) < 6 and dico["titre"] != ' None ') and dico["titre_compare"] != ' None ':
#             a = print("la distance entre", dico["titre"], "et", dico["titre_compare"], "est egal a", dico["distance"],
#                       "l'indice x est", dico["x"], "l'indice i est", dico["i"])

#             #ed2 = nltk.edit_distance(listee[dico["x"]], listee[dico["i"]])
#             #print("la distance par rapport au personal name entre", listee[dico["x"]], "et", listee[dico["i"]], "est",
#             #      ed2)

# # Jaccard distance


# for x in range(len(valeur)):
#     for i in range(x + 1, len(valeur)):
#         ed = nltk.jaccard_distance(set(valeur[x]), set(valeur[i]))
#         dico = {"titre": valeur[x], "titre_compare": valeur[i], "distance": ed, "x": x, "i": i}
#         a = (
#         (dico["titre"]), "&&", (dico["titre_compare"]), "&&", (dico["distance"]), "&&", (dico["x"]), "&&", (dico["i"]))

#         if ((dico["distance"]) < 0.32 and dico["titre"] != ' None ') and dico["titre_compare"] != ' None ':
#             a = print("la distance entre", dico["titre"], "et", dico["titre_compare"], "est egal a", dico["distance"],
#                       "et l'indice x est :", dico["x"], "et l'indice i est :", dico["i"])

#             ed2 = nltk.jaccard_distance(set(listee[dico["x"]]), set(listee[dico["i"]]))
#             print("la distance par rapport au personal name entre", listee[dico["x"]], "et", listee[dico["i"]], "est",
#                   ed2)
# '''


def get_author_name(author_id):
    c.execute("SELECT NAME FROM AUTHORS WHERE ID = ?", (author_id,))
    try:
        d = c.fetchone()['NAME']
        return d
    except TypeError:
        return None

def get_author_alt_names(author_id):
    c.execute("SELECT NAME FROM AUTHOR_ALT_NAME WHERE ID_AUTHOR = ?", (author_id,))
    try:
        d = c.fetchone()['NAME']
        return d
    except TypeError:
        return None

def dist_author_name(author_id_1, author_id_2):
    result = 0
    author_name_1 = get_author_name(author_id_1)
    author_name_2 = get_author_name(author_id_2)
    if author_name_1 is None or author_name_2 is None:
        print(author_name_1, " ", author_name_2)
        return None
    author_alt_names_1 = get_author_alt_names(author_id_1)
    author_alt_names_2 = get_author_alt_names(author_id_2)
    ed = nltk.edit_distance(author_name_1, author_name_2)
    if author_alt_names_1 is not None:
        ed2 = nltk.edit_distance(author_name_1, author_alt_names_1)
        return ed2 / (abs(len(author_name_1)) + abs(len(author_alt_names_1)))
    try:
        result = ed / (abs(len(author_name_1)) + abs(len(author_name_2)))
        return result
    except ZeroDivisionError:
        return None



def sigmoid(x):
    return 1 / (1 + exp(-x))


def dist_year(y1, y2):
    if not y1 or not y2:
        return None
    return (2 * sigmoid(abs(y2 - y1) / 4) - 1)


# input: une date comme  string avec toute les variations qu'on peut trouver dans la bd
# output: une date de type date ou None is la date d'entrée est mal formée ou manquante
def parse_db_str(d_str):
    if not d_str:
        return None

    try:
        return datetime.strptime(d_str, '%Y').year
    except:
        pass

    try:
        return datetime.strptime(d_str, '%Y-%m-%d').year

    except:
        pass

    return None


if __name__ == "__main__":
    assert parse_db_str('1990') == 1990
    assert parse_db_str('1990-04-30') == 1990


def get_author_birth_date(author_id):
    c.execute("SELECT BIRTH_DATE FROM AUTHORS WHERE ID=?", (author_id,))
    try:
        d_str = c.fetchone()['BIRTH_DATE']
        return parse_db_str(d_str)
    except TypeError:
        return None


def get_author_death_date(author_id):
    c.execute("SELECT DEATH_DATE FROM AUTHORS WHERE ID=?", (author_id,))
    try:
        d_str = c.fetchone()['DEATH_DATE']
        return parse_db_str(d_str)
    except TypeError:
        return None


def dist_author_date(author_id_1, author_id_2):
    author_date_1 = get_author_birth_date(author_id_1)
    author_date_2 = get_author_birth_date(author_id_2)
    author_date_death_1 = get_author_death_date(author_id_1)
    author_date_death_2 = get_author_death_date(author_id_2)
    if author_date_1 is not None and author_date_2 is not None and (
            author_date_death_1 is None or author_date_death_2 is None):
        return dist_year(author_date_1, author_date_2)
    if author_date_death_1 is not None and author_date_death_2 is not None:
        return dist_year(author_date_death_1, author_date_death_2)
    if author_date_1 is not None and author_date_2 is not None and author_date_death_1 is not None and author_date_death_2 is not None:
        return (dist_year(author_date_1, author_date_2) + dist_year(author_date_death_1, author_date_death_2)) / 2
    if (author_date_1 is None or author_date_2 is None) and (
            author_date_death_1 is None or author_date_death_2 is None):
        return None


def dist_author(author_id_1, author_id_2):
    author_name = dist_author_name(author_id_1, author_id_2)
    author_date = dist_author_date(author_id_1, author_id_2)
    if author_name is None or author_date is None:
        return None
    if author_name is not None and author_date is None:
        return author_name
    if author_name is None and author_date is not None:
        return author_date
    if author_name is not None and author_date is not None:
        return (author_name + author_date) / 2


for x in range(len(tab_id2)):
    for i in range(x + 1, len(tab_id2)):
        if dist_author(tab_id2[x],tab_id2[i]) is not None:
            print(dist_author(tab_id2[x],tab_id2[i]))

def get_author_birth_date(author_id):
    c.execute("SELECT BIRTH_DATE FROM AUTHOR WHERE ID=?", (author_id,))
    d_str = c.fetchOne()['BIRTH_DATE']
    return parse_db_str(d_str)


if __name__ == '__main__':
    print(dist_year(1999, 1993))
    print(dist_year(1990, 1993))
    print(dist_year(1990, 1991))
    # assert dist_date(datetime.strptime('1990','%Y'),datetime.strptime('1990','%Y')) == 0.0
    # assert dist_date(datetime.strptime('1990','%Y'),datetime.strptime('1990-01-01','%Y-%d-%m')) <= 0.1
    # print(dist_date(datetime.strptime('1990','%Y'),datetime.strptime('1990-30-04','%Y-%d-%m')))
    # print(dist_date(datetime.strptime('1990','%Y'),datetime.strptime('1991-30-04','%Y-%d-%m')))
    # print(dist_date(datetime.strptime('1990','%Y'),None))