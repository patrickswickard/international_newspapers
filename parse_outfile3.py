import os
import json
import re
import requests
import csv

confirmed_file = open("outfile_wpconfirmed.txt",'r')

confirmed_list = json.loads(confirmed_file.read())

confirmed_file.close()

spam_set = set()

with open("spam.txt",'r') as spam_file:
  reader = csv.reader(spam_file)
  for row in reader:
     spam_set.add(row[0])
spam_file.close()

#unresponsive_list = []
#wordpress_site_list = []
#wordpress_nonsite_list = []

wordpress_legitimate_list = []

count = 0
for thisfilename in confirmed_list:
    count += 1
    print(thisfilename)
    print(count)
    if thisfilename in spam_set:
        print("THIS IS SPAM SITE")
    else:
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
      wordpress_legitimate_list.append(thisfilename)
      #inp = input('press any key to continue')
      print('************')
outfile = open("outfile_wplegit.txt",'w')
outfile.write(json.dumps(wordpress_legitimate_list))
outfile.close
print(wordpress_legitimate_list)
