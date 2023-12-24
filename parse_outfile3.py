"""Explore confirmed spam etc"""
import json
import csv

with open('outfile_wpconfirmed.txt','r',encoding='utf-8') as myinfile:
  confirmed_list = json.loads(myinfile.read())

spam_set = set()

with open("spam.txt",'r',encoding='utf-8') as myinfile:
  reader = csv.reader(myinfile)
for row in reader:
  spam_set.add(row[0])

wordpress_legitimate_list = []

count = 0
for thisfilename in confirmed_list:
  count += 1
  print(thisfilename)
  print(count)
  if thisfilename in spam_set:
    print("THIS IS SPAM SITE")
  else:
    with open('wikidata/' + thisfilename,'r',encoding='utf-8') as myinfile:
      thishash = json.loads(myinfile.read())
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
#outfile = open("outfile_wplegit.txt",'w')
#outfile.write(json.dumps(wordpress_legitimate_list))
#outfile.close
with open("outfile_wplegit.txt",'w',encoding='utf-8') as myoutfile:
  myoutfile.write(json.dumps(wordpress_legitimate_list))
print(wordpress_legitimate_list)
