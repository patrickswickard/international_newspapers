"""Script to explore confirmed sites"""
import json

with open('outfile_wpconfirmed.txt','r',encoding='utf-8') as myinfile:
  confirmed_list = json.loads(myinfile.read())

COUNT = 299
for thisfilename in confirmed_list[COUNT:100000]:
  count += 1
  print(thisfilename)
  print(count)
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
  inp = input('press any key to continue')
  print('************')
