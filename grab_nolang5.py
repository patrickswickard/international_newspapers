"""Script to find wikidata without language"""
import json
import re


with open('wikidata_query_result.json','r',encoding='utf-8') as myinfile:
  query_result = json.loads(myinfile.read())

language_hash = {}

biglist = query_result['results']['bindings']
for thisitem in biglist:
  id1 = thisitem.get('item',{}).get('value')
  id2 = re.sub('http://www.wikidata.org/entity/','',id1)
  print(id1)
  print(id2)
  language1 = thisitem.get('languageLabel',{}).get('value')
  language2 = thisitem.get('language',{}).get('value')
  print(language1)
  print(language2)
  if language2:
    language3 = re.sub('http://www.wikidata.org/entity/','',language2)
    language_hash[id2] = language1 + ' (' + str(language3) + ')'
  else:
    language_hash[id2] = language1

with open('outfile_wplegit.txt','r',encoding='utf-8') as myinfile:
  legit_list = json.loads(myinfile.read())

wordpress_legitimate_list = []

count = 0
langhash = {}
print


def fetch_language(thisid):
  """Fetch language from id"""
  return language_hash[thisid]

for thisfilename in legit_list:
  with open('wikidata/' + thisfilename,'r',encoding='utf-8') as myinfile:
    thishash = json.loads(myinfile.read())
  #print(thisfilename)
  myid = thishash['wikibase']
  language = thishash['wikidata'].get('language of work or name (P407)','None')
  #print(language)
  #language = thishash['wikidata']['language of work or name (P407)']
  if isinstance(language,list):
    language = language[0]
  if language == 'None':
    language = fetch_language(myid)
  print(language)
  langhash[language] = language.get(language,0) + 1
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
  #inp = input('press any key to continue')
  print('************')
#outfile = open("outfile_wplegit.txt",'w')
#outfile.write(json.dumps(wordpress_legitimate_list))
#outfile.close
#print(wordpress_legitimate_list)
langcount = 0
for key, value in langhash.items():
  print(str(key) + ' | ' + str(value))
  langcount += value
print(langcount)
with open('language_hash.json','w',encoding='utf-8') as myoutfile:
  myoutfile.write(json.dumps(language_hash))
