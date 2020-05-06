import csv
import sys
import json
import sqlite3

COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = '../data/small_works.txt'
# INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
# DB_FILE = 'opendata.db'
# DB_FILE = 'databases.db'
DB_FILE = '../bdd/databases.db'
# DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema-works.sql'

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript(open(DB_SCHEMA, 'r').read())

for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
    j = json.loads(record['json'])

    subjects = ''
    tab_sub = []
    if 'subjects' in j:
        for n in j['subjects']:
            tab_sub.append(n)

        subjects = str(tab_sub)
    else:
        subjects = None

    subject_places = ''
    tab_subject_places = []
    if 'sucject_places' in j:
        for n in j['subject_places']:
            tab_subject_places.append(n)
            subject_places = str(tab_subject_places)
    else:
        subject_places = None

    subject_times = ''
    tab_subject_times = []
    if 'subject_times' in j:
        for n in j['subject_times']:
            tab_subject_times.append(n)
            subject_times = str(tab_subject_times)
    else:
        subject_times = None

    subject_people = ''
    tab_subject_people = []
    if 'subject_people' in j:
        for n in j['subject_people']:
            tab_subject_people.append(n)
            subject_people = str(tab_subject_people)
    else:
        subject_people = None

    description = ''
    if 'description' in j and 'value' in j['description']:
        description = j['description']['value']
    else:
        description = None

    dewey_number = ''
    tab_dewey_number = []
    if 'dewey_number' in j:
        for n in j['dewey_number']:
            tab_dewey_number.append(n)
            dewey_number = str(tab_dewey_number)
    else:
        dewey_number = None

    lc_classifications = ''
    tab_lc = []
    if 'lc_classifications' in j:
        for n in j['lc_classifications']:
            tab_lc.append(n)
            lc_classifications = str(tab_lc)
    else:
        lc_classifications = None

    other_titles = ''
    tab_other_titles = []
    if 'other_titles' in j:
        for n in j['other_titles']:
            tab_other_titles.append(n)
            other_titles = str(tab_other_titles)
    else:
        other_titles = None

    covers = ''
    tab_covers = []
    if 'covers' in j:
        for n in j['covers']:
            tab_covers.append(n)
            covers = str(tab_covers)
    else:
        covers = None
    
    
    tab_author =  []
    tab_role = []
    tab_as = []
    author = ""
    author_role = ""
    author_as = ""
    if 'authors' in j:
        for n in j['authors']:
            dico = {'author': n['author']}
            #dico2 = {'role': n['role']}
            #dico3 = {'as': n['as']}
            tab_author.append(dico['author'])
            #tab_role.append(dico2['role'])
            #tab_as.append(dico3['as'])

        author = str(tab_author)
        #author_role = str(tab_role)
        #author_as = str(tab_as)

    else:
        author = None
        #author_role = None
        #author_as = None
        
        
        
        
        
    tab_translated_language =  []
    tab_translated_text = []
    translated_titles_language = ""
    translated_titles_text = ""
    if 'translated_titles' in j:
        for n in j['translated_titles']:
            dico = {'language': n['language']}
            dico2 = {'text': n['text']}
            tab_author.append(dico['language'])
            tab_role.append(dico2['text'])

        translated_titles_language = str(tab_translated_language)
        translated_titles_text = str(tab_translated_text)

    else:
        translated_titles_language = None
        translated_titles_text = None
        
        
    tab_original_language_name =  []
    tab_original_language_code = []
    tab_original_language_library = []
    original_language_name = ""
    original_language_code = ""
    original_language_library = ""
    if 'original_languages' in j:
        for n in j['original_languages']:
            dico = {'name': n['name']}
            dico2 = {'code': n['code']}
            dico3 = {'library_of_congress_name': n['library_of_congress_name']}
            tab_original_language_name.append(dico['name'])
            tab_original_language_code.append(dico2['code'])
            tab_original_language_library.append(dico3['library_of_congress_name'])

        original_language_name = str(tab_original_language_name)
        original_language_code = str(tab_original_language_code)
        original_language_library = str(tab_original_language_library)

    else:
        original_language_name = None
        original_language_code = None
        original_language_library = None
        
    links_url = ""
    links_title = ""
    tab_url = ""
    tab_title = ""
    if 'links' in j:
        for link in j['links']:
            dico = {'url': link['url']}
            dico2 = {'title': link['title']}
            tab_url.append(dico['url'])
            tab_title.append(dico2['title'])

        links_url = str(tab_url)
        links_title = str(tab_title)

    else:
        links_url = None
        links_title = None


    c.execute('INSERT INTO WORKS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
              [record['key'],
               j.get('title'),
               j.get('subtitle'),
               author,
               translated_titles_language,
               translated_titles_text,
               subjects,
               subject_places,
               subject_times,
               subject_people,
               description,
               dewey_number,
               lc_classifications,
               j.get('first_sentence'),
               original_language_name,
               original_language_code,
               original_language_library,
               other_titles,
               j.get('first_publish_date'),
               links_url,
               links_title,
               j.get('notes'),
               j.get('cover_edition'),
               covers])
db.commit()

print(subjects)