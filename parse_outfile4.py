"""Script to explore legit sites"""
import json

with open('outfile_wplegit.txt','r',encoding='utf-8') as myinfile:
  legit_list = json.loads(myinfile.read())

wordpress_legitimate_list = []

count = 0
for thisfilename in legit_list:
  count += 1
  print(thisfilename)
  print(count)
  with open('wikidata/' + thisfilename,'r',encoding='utf-8') as myinfile:
    thishash = json.loads(myinfile.read())
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
  language = thishash['wikidata'].get('language of work or name (P407)','None')
  print(language)
  if isinstance(language,list):
    language = language[0]
  full_url = base_url + '/wp-json/wp/v2/posts?search='
  print(full_url)
  wordpress_legitimate_list.append(thisfilename)
  print('************')
