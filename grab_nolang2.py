import os
import json
import re
import requests
import csv

legit_file = open("outfile_wplegit.txt",'r')

legit_list = json.loads(legit_file.read())

legit_file.close()

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
    thisfile = open('wikidata/' + thisfilename)
    thishash = json.loads(thisfile.read())
    thisfile.close()
    #print(thisfilename)
    id = thishash['wikibase']
    mystring = mystring + 'wd:' + id
    mystring = mystring + """))
SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
}"""
    print(mystring)
    outfile = open("oneitem2.sparql",'w')
    outfile.write(mystring)
    outfile.close
    os.system('wikidata-dl -i -d wikidata3 oneitem2.sparql')
#print(wordpress_legitimate_list)
#for i in langhash.keys():
#    print(str(i) + '|' + str(langhash[i]))
