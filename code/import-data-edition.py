import csv
import sys
import json
import sqlite3

COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = '../data/small_edition.txt'
# INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
# DB_FILE = 'opendata.db'
# DB_FILE = 'databases.db'
DB_FILE = '../bdd/databases.db'
# DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema-edition.sql'
db = sqlite3.connect(DB_FILE)

c = db.cursor()

c.executescript(open(DB_SCHEMA, 'r').read())

for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
    j = json.loads(record['json'])

    other_titles = ''
    tab_other_titles = []
    if 'other_titles' in j:
        for n in j['other_titles']:
            tab_other_titles.append(n)
            other_titles = str(tab_other_titles)
    else:
        other_titles = None

    description = ''
    if 'description' in j and 'value' in j['description']:
        description = j['description']['value']
    else:
        description = None
        
    first_sentence = ''
    if 'first_sentence' in j and 'value' in j['first_sentence']:
        first_sentence = j['first_sentence']['value']
    else:
        first_sentence = None

    notes = ''
    if 'notes' in j and 'value' in j['notes']:
        notes = j['notes']['value']
    else:
        notes = None

    genres = ''
    tab_genres = []
    if 'genres' in j:
        for n in j['genres']:
            tab_genres.append(n)
            genres = str(tab_genres)
    else:
        genres = None

    work_titles = ''
    tab_work_titles = []
    if 'work_titles' in j:
        for n in j['work_titles']:
            tab_work_titles.append(n)
            work_titles = str(tab_work_titles)
    else:
        work_titles = None

    series = ''
    tab_series = []
    if 'series' in j:
        for n in j['series']:
            tab_series.append(n)
            series = str(tab_series)
    else:
        series = None

    subjects = ''
    tab_subjects = []
    if 'subjects' in j:
        for n in j['subjects']:
            tab_subjects.append(n)
            subjects = str(tab_subjects)
    else:
        subjects = None

    lccn = ''
    tab_lccn = []
    if 'lccn' in j:
        for n in j['lccn']:
            tab_lccn.append(n)
            lccn = str(tab_lccn)
    else:
        lccn = None

    oclc_numbers = ''
    tab_oclc = []
    if 'oclc_numbers' in j:
        for n in j['oclc_numbers']:
            tab_oclc.append(n)
            oclc_numbers = str(tab_oclc)
    else:
        oclc_numbers = None

    isbn_10 = ''
    tab_isbn10 = []
    if 'isbn_10' in j:
        for n in j['isbn_10']:
            tab_isbn10.append(n)
            isbn_10 = str(tab_isbn10)
    else:
        isbn_10 = None

    isbn_13 = ''
    tab_isbn13 = []
    if 'isbn_13' in j:
        for n in j['isbn_13']:
            tab_isbn13.append(n)
            isbn_13 = str(tab_isbn13)
    else:
        isbn_13 = None

    dewey_decimal_class = ''
    tab_dewey_decimal_class = []
    if 'dewey_decimal_class' in j:
        for n in j['dewey_decimal_class']:
            tab_dewey_decimal_class.append(n)
            dewey_decimal_class = str(tab_dewey_decimal_class)
    else:
        dewey_decimal_class = None

    lc_classifications = ''
    tab_lc = []
    if 'lc_classifications' in j:
        for n in j['lc_classifications']:
            tab_lc.append(n)
            lc_classifications = str(tab_lc)
    else:
        lc_classifications = None

    contributions = ''
    tab_contributions = []
    if 'contributions' in j:
        for n in j['contributions']:
            tab_contributions.append(n)
            contributions = str(tab_contributions)
    else:
        contributions = None

    publish_places = ''
    tab_publish_places = []
    if 'publish_places' in j:
        for n in j['publish_places']:
            tab_publish_places.append(n)
            publish_places = str(tab_publish_places)
    else:
        publish_places = None

    publishers = ''
    tab_publishers = []
    if 'publishers' in j:
        for n in j['publishers']:
            tab_publishers.append(n)
            publishers = str(tab_publishers)
    else:
        publishers = None

    distributors = ''
    tab_distributors = []
    if 'distributors' in j:
        for n in j['distributors']:
            tab_distributors.append(n)
            distributors = str(tab_distributors)
    else:
        distributors = None

    location = ''
    tab_location = []
    if 'location' in j:
        for n in j['location']:
            tab_location.append(n)
            location = str(tab_location)
    else:
        location = None

    uris = ""
    tab_uris = []
    if 'uris' in j:
        for n in j['uris']:
            tab_uris.append(n)
            uris = str(tab_uris)
    else:
        uris = None

    source_records = ""
    tab_source_records = []
    if 'source_records' in j:
        for n in j['source_records']:
            tab_source_records.append(n)
            source_records = str(tab_source_records)
    else:
        source_records = None

    uri_descriptions = ""
    tab_uri_descriptions = []
    if 'uri_descritions' in j:
        for n in j['uri_descriptions']:
            tab_uri_descriptions.append(n)
            uri_descriptions = str(tab_uri_descriptions)
    else:
        uri_descriptions = None

    author_key = ""
    tab_author_key = []
    if 'authors' in j:
        for n in j['authors']:
            dico = {'key': n['key']}
            tab_author_key.append(dico['key'])
    
        author_key = str(tab_author_key)
    
    else:
        author_key = None
        
    
    languages_name = ""
    tab_languages_name = []
    language_code = ""
    tab_language_code = []
    language_library = ""
    tab_language_library = []
    language_key = ""
    tab_key_language = []
    if 'languages' in j:
        for n in j['languages']:
            #dico = {'name': n['name']}
            #dico2 = {'code': n['code']}
            #dico3 = {'library_of_congress_name': n['library_of_congress_name']}
            #tab_languages_name.append(dico['name'])
            #tab_language_code.append(dico['code'])
            #tab_language_library.append(dico['library_of_congress_name'])
            dico = {'key': n['key']}


        #languages_name = str(tab_languages_name)
        #language_code = str(tab_language_code)
        #language_library = str(tab_language_library)
        language_key = str(tab_key_language)

    else:
        #languages_name = None
        #language_code = None
        #language_library = None
        language_key = None

    toc_class = ""
    tab_toc_class = []
    toc_label = ""
    tab_toc_label = []
    toc_title = ""
    tab_toc_title = []
    toc_pagenum = ""
    tab_toc_pagenum = []
    if 'tables_of_contents' in j:
        for n in j['table_of_contents']:
            dico = {'class': n['class']}
            dico2 = {'label': n['label']}
            dico3 = {'title': n['title']}
            dico4 = {'pagenum': n['pagenum']}
            tab_toc_class.append(dico['class'])
            tab_toc_label.append(dico['label'])
            tab_toc_title.append(dico['title'])
            tab_toc_pagenum.append(dico['pagenum'])


            toc_class = str(tab_toc_class)
            toc_label = str(tab_toc_label)
            toc_title = str(tab_toc_title)
            toc_pagenum = str(tab_toc_pagenum)

    else:
        toc_class = None
        toc_label = None
        toc_title = None
        toc_pagenum = None

    collections_name = ""
    tab_collections_name = []
    if 'collections' in j:
        for n in j['collections']:
            dico = {'name': n['name']}
            tab_collections_name.append(dico['name'])

        collections_name = str(tab_collections_name)

    else:
        collections_name = None

    works_key = ""
    tab_work_key = []
    if 'works' in j:
        for n in j['works']:
            dico = {'key': n['key']}
            tab_work_key.append(dico['key'])

        work_key = str(tab_work_key)

    else:
        work_key = None

    tab_translated_name = []
    tab_translated_code = []
    tab_translated_library = []
    translated_from_name = ""
    translated_from_code = ""
    translated_from_library = ""
    translated_key = ""
    tab_translated_key = []
    if 'translated_from' in j:
        for n in j['translated_from']:
            #dico = {'name': n['name']}
            #dico2 = {'code': n['code']}
            #dico3 = {'library_of_congress_name': n['library_of_congress_name']}
            dico = {'key': n['key']}
            #tab_translated_name.append(dico['name'])
            #tab_translated_code.append(dico2['code'])
            #tab_translated_library.append(dico3['library_of_congress_name'])
            tab_translated_key.append(dico['key'])

        #translated_from_name = str(tab_translated_name)
        #translated_from_code = str(tab_translated_code)
        #translated_from_library = str(tab_translated_library)
        translated_key = str(tab_translated_key)

    else:
        #translated_from_name = None
        #translated_from_code = None
        #translated_from_library = None
        translated_key = None

    scan_records_key = ""
    tab_scan_records_key = []
    if 'scan_records' in j:
        for n in j['scan_records']:
            dico = {'key': n['key']}
            tab_scan_records_key.append(dico['key'])

        scan_records_key = str(tab_scan_records_key)

    else:
        scan_records_key = None

    volume_ia_id = ""
    tab_volume_ia_id = []
    tab_volume_number = []
    volume_number = ""
    if 'volumes' in j:
        for n in j['volumes']:
            dico = {'ia_id': n['ia_id']}
            dico2 = {'volume_number': n['volume_number']}
            tab_volume_ia_id.append(dico['ia_id'])
            tab_volume_number.append(dico2['volume_number'])

        volume_ia_id = str(tab_volume_ia_id)
        volume_number = str(tab_volume_number)

    else:
        volume_ia_id = None
        volume_number = None

    c.execute('INSERT INTO EDITION VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        [record['key'],
        j.get('title'),
        j.get('title_prefix'),
        j.get('subtitle'),
        other_titles,
        author_key,
        j.get('by_statement'),
        j.get('publish_date'),
        j.get('copyright_date'),
        j.get('edition_name'),
        language_key,
        description,
        notes,
        genres,
        toc_class,
        toc_label,
        toc_title,
        toc_pagenum,
        work_titles,
        series,
        j.get('physical_dimensions'),
        j.get('physical_format'),
        j.get('number_of_pages'),
        subjects,
        j.get('pagination'),
        lccn,
        j.get('ocaid'),
        oclc_numbers,
        isbn_10,
        isbn_13,
        dewey_decimal_class,
        lc_classifications,
        contributions,
        publish_places,
        j.get('publish_country'),
        publishers,
        distributors,
        first_sentence,
        j.get('weight'),
        location,
        j.get('scan_on_demand'),
        collections_name,
        uris,
        uri_descriptions,
        j.get('translation_of'),
        work_key,
        source_records,
        translated_key,
        scan_records_key,
        volume_ia_id,
        volume_number,
        j.get('accompanying_material')])
db.commit()