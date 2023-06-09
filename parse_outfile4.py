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
for thisfilename in legit_list:
    count += 1
    print(thisfilename)
    print(count)
    thisfile = open('wikidata/' + thisfilename)
    thishash = json.loads(thisfile.read())
    thisfile.close()
    title = thishash['title']
    print(title)
    description = thishash['description']
    print(description)
    base_url = thishash['claims']['P856']
    if type(base_url) is list:
        base_url = base_url[0]
    base_url2 = thishash['wikidata']['official website (P856)']
    if type(base_url2) is list:
        base_url2 = base_url2[0]
    if base_url != base_url2:
      print('Something went wrong')
      print(base_url)
      print(base_url2)
      break
    print(base_url)
    print(base_url2)
    #language = thishash['wikidata']['language of work or name (P407)']
    language = thishash['wikidata'].get('language of work or name (P407)','None')
    print(language)
    #language = thishash['wikidata']['language of work or name (P407)']
    if type(language) is list:
        language = language[0]
    full_url = base_url + '/wp-json/wp/v2/posts?search='
    print(full_url)
    wordpress_legitimate_list.append(thisfilename)
    #inp = input('press any key to continue')
    print('************')
#outfile = open("outfile_wplegit.txt",'w')
#outfile.write(json.dumps(wordpress_legitimate_list))
#outfile.close
#print(wordpress_legitimate_list)
