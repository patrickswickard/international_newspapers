"""Script to find wikidata without language"""
import json

with open('outfile_wplegit.txt','r',encoding='utf-8') as myinfile:
  legit_list = json.loads(myinfile.read())

wordpress_legitimate_list = []

count = 0
langhash = {}
for thisfilename in legit_list:
  with open('wikidata/' + thisfilename,'r',encoding='utf-8') as myinfile:
    thishash = json.loads(myinfile.read())
  myid = thishash['wikibase']
  language = thishash['wikidata'].get('language of work or name (P407)','None')
  if isinstance(language,list):
    language = language[0]
  if not language == 'None':
    print(language)
    langhash[language] = langhash.get(language,0) + 1
  count += 1
  print(count)
  print('https://www.wikidata.org/wiki/' + myid)
  title = thishash['title']
  print(title)
  description = thishash['description']
  print(description)
  base_url = thishash['claims']['P856']
  if isinstance(base_url,list):
    base_url = base_url[0]
  base_url2 = thishash['wikidata']['official website (P856)']
  if isinstance(base_url2,list):
    base_url2 = base_url2[0]
  if base_url != base_url2:
    print('Something went wrong')
    print(base_url)
    print(base_url2)
    break
  print(base_url)
  print(base_url2)
  full_url = base_url + '/wp-json/wp/v2/posts?search='
  print(full_url)
  wordpress_legitimate_list.append(thisfilename)
  print('************')
#for i in langhash.keys():
#  print(str(i) + '|' + str(langhash[i]))
for key,value in langhash.items():
  print(str(key) + '|' + str(value))
