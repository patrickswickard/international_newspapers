import os
import json
import re
import requests

outfile = open("outfile.txt",'r')

outlist = json.loads(outfile.read())

outfile.close()

taghash = {} 

count = 0
for thisfilename in outlist:
    count += 1
    print(count)
    thisfile = open('wikidata/' + thisfilename)
    thishash = json.loads(thisfile.read())
    thisfile.close()
    title = thishash['title']
    print(title)
    description = thishash['description']
    print(description)
    base_url = thishash['claims']['P856'][0]
    print(base_url)
    full_url = base_url + '/wp-json/wp/v2/posts?search='
    print(full_url)
    try:
      exhtml = thishash['exhtml']
      print(exhtml)
    except:
      pass
    print('************')
    for thislabel in thishash['labels']:
        if re.search(r"^Q",thislabel):
          label = thishash['labels'][thislabel]
          taghash[label] = 1
    print('************')
taglist = list(taghash.keys())
print(taglist)
for thistag in taglist:
    print(thistag)
