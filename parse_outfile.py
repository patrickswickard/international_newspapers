import os
import json
import re
import requests

outfile = open("outfile.txt",'r')

outlist = json.loads(outfile.read())

outfile.close()

for thisfilename in outlist:
    thisfile = open('wikidata/' + thisfilename)
    thishash = json.loads(thisfile.read())
    thisfile.close()
    title = thishash['title']
    print(title)
    description = thishash['description']
    print(description)
    base_url = thishash['claims']['P856'][0]
    print(base_url)
    print('************')
