import csv
import sys
import json
import sqlite3

import nltk

COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = '../data/small-authors.txt'
# INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
# DB_FILE = 'opendata.db'
DB_FILE = '../bdd/databases.db'
# DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema.sql'

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript(open(DB_SCHEMA, 'r').read())

# # keys = set()
# i = 1
## try:
#     for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
#         #print(record['type'],record['key'],record['revision'])
#         # key = record['key']
#         # if key in keys:
#         #     print("BAM",key,record)
#         #     sys.exit(1)
#         # keys.add(key)
#         i += 1
# except:
#



for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
    j = json.loads(record['json'])

    if 'bio' in j and 'value' in j['bio']:
        bio = j['bio']['value']
    else:
        bio = None


    uris = ""
    tab_uris = []
    if 'uris' in j:
        for n in j['uris']:
            tab_uris.append(n)
            uris = str(tab_uris)
    else:
        uris = None


    maybe = []
    title = []

    if 'links' in j:
        for link in j['links']:
            dico = {'url': link['url']}
            dico2 = {'title': link['title']}
            maybe.append(dico['url'])
            title.append(dico2['title'])

        links = str(maybe)
        links_title = str(title)

    else:
        links = None
        links_title = None

    c.execute('INSERT INTO AUTHORS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
              [record['key'],
               j.get('name'),
               j.get('eastern_order'),
               j.get('personal_name'),
               j.get('enumeration'),
               j.get('title'),
               bio,
               uris,
               j.get('location'),
               j.get('birth_date'),
               j.get('death_date'),
               j.get('date'),
               j.get('wikipedia'),
               links,
               links_title])

    if 'alternate_names' in j:
        for alt_name in j['alternate_names']:
            c.execute('INSERT INTO AUTHOR_ALT_NAME VALUES (?,?)',
                      [record['key'], alt_name])

db.commit()

