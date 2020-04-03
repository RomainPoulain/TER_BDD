import re
import json
import pprint


bio_regex = re.compile(
    r"""
("bio":\s*{)   # bio field start
(.*?)          # content
(},)           # bio field end
(?=\s*(?:"\w+"|}))  # followed by another one or the json end
""",
    flags=re.VERBOSE | re.DOTALL)

value_regex = re.compile(
    r"""
("value":\s*")   # value field start
(.*?)            # content
("\s*\Z)         # value field end + end of string
""",
    flags=re.VERBOSE | re.DOTALL)


def normalize_value(mo):
    start, content, end = mo.group(1, 2, 3)
    content = content.replace('"', '\\"')
    return start + content + end


def normalize_bio(mo):
    start, content, end = mo.group(1, 2, 3)
    content = value_regex.sub(normalize_value, content)
    return start + content + end

messy_json = """
{ 
  "bio":{ 
    "type":"/type/text",
    "value":"> "Eversley, William Pinder, B.C.L. Queen's Coll., Oxon, M.A., a member of the South-eastern circuit, reporter for Law Times in Queen's Bench division, a student of the Inner Temple 14 April, 1874 (then aged 23), called to the bar 25 April, 1877 (eldest son of William Eversley, Esq., of London); born u2060, 1851. rn> rn> 7, King's Bench Walk, Temple, E.C." rn> ...[in Foster's Men at the Bar][1]rnrnrn rnrn[1]: https://en.wikisource.org/wiki/Men-at-the-Bar/Eversley,_William_Pinder "Men at the Bar""
  },
  "name":"William Pinder Eversley",
  "created":{ 
    "type":"/type/datetime",
    "value":"2008-04-01T03:28:50.625462"
  },
  "death_date":"1918",
  "photos":[ 
    6897255,
    6897254
  ],
  "last_modified":{ 
    "type":"/type/datetime",
    "value":"2018-07-31T15:39:07.982159"
  },
  "latest_revision":6,
  "key":"/authors/OL1003081A",
  "birth_date":"1851",
  "personal_name":"William Pinder Eversley",
  "type":{ 
    "key":"/type/author"
  },
  "revision":6
}"""


result = bio_regex.sub(normalize_bio, messy_json)
obj = json.loads(result)

print(result)