"""Script to find wikidata without language"""
import os
import json

with open('outfile_wplegit.txt','r',encoding='utf-8') as myinfile:
  legit_list = json.loads(myinfile.read())

wordpress_legitimate_list = []

count = 0
langhash = {}
for thisfilename in legit_list:
  count += 1
  print(count)
  mystring = """# https://query.wikidata.org/
#defaultView:Table
SELECT ?item ?itemLabel ?country ?countryLabel ?place ?placeLabel ?language ?languageLabel ?pic ?offurl
WHERE
{
?item wdt:P31 wd:Q11032 .
#OPTIONAL {?item wdt:P17 ?country .}
#OPTIONAL {?item wdt:P291 ?place .}
#OPTIONAL {?item wdt:P407 ?language .}
#OPTIONAL {?item wdt:P154 ?pic .}
?item wdt:P856 ?offurl
#FILTER(?item = wd:Q12719396)
FILTER(?item in (wd:Q12719396, """
  with open('wikidata/' + thisfilename,'r',encoding='utf-8') as myinfile:
    thishash = json.loads(myinfile.read())
  myid = thishash['wikibase']
  mystring = mystring + 'wd:' + myid
  mystring = mystring + """))
SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
}"""
  print(mystring)
  with open('oneitem2.sparql','w',encoding='utf-8') as myoutfile:
    myoutfile.write(mystring)
  os.system('wikidata-dl -i -d wikidata3 oneitem2.sparql')
