"""Get information from saved wikidata query result etc"""
import json
import re

with open('wikidata_query_result.json','r',encoding='utf-8') as myinfile:
  query_result = json.loads(myinfile.read())

language_hash = {}
offurl_hash = {}
country_hash = {}
place_hash = {}

biglist = query_result['results']['bindings']
for thisitem in biglist:
  id1 = thisitem.get('item',{}).get('value')
  id2 = re.sub('http://www.wikidata.org/entity/','',id1)
  #print(id1)
  #print(id2)
  language1 = thisitem.get('languageLabel',{}).get('value')
  language2 = thisitem.get('language',{}).get('value')
  #print(language1)
  #print(language2)
  if language2:
    language3 = re.sub('http://www.wikidata.org/entity/','',language2)
    language_hash[id2] = language1 + ' (' + str(language3) + ')'
  else:
    language_hash[id2] = language1
  thisoffurl = thisitem.get('offurl',{}).get('value')
  offurl_hash[id2] = thisoffurl
  #print(thisoffurl)
  thiscountry = thisitem.get('countryLabel',{}).get('value')
  country_hash[id2] = thiscountry
  #print(thiscountry)
  thisplace = thisitem.get('placeLabel',{}).get('value')
  place_hash[id2] = thisplace
  #print(thisplace)

with open('outfile_wplegit.txt','r',encoding='utf-8') as myinfile:
  legit_list = json.loads(myinfile.read())

wordpress_legitimate_list = []

count = 0
langhash = {}

qidhash = {}
for thisfilename in legit_list:
#  thisfile = open('wikidata/' + thisfilename)
#  thishash = json.loads(thisfile.read())
#  thisfile.close()
  with open('wikidata/' + thisfilename,'r',encoding='utf-8') as myinfile:
    thishash = json.loads(myinfile.read())
  #print(thisfilename)
  myid = thishash['wikibase']
  language = thishash['wikidata'].get('language of work or name (P407)','None')
  #print(language)
  #language = thishash['wikidata']['language of work or name (P407)']
#  if type(language) is list:
  if isinstance(language,list):
    language = language[0]
  if not language == 'None':
    if language in list(langhash.keys()):
      langhash[language] += 1
    else:
      langhash[language] = 1
  else:
    language = language_hash[myid]
    if language in list(langhash.keys()):
      langhash[language] += 1
    else:
      langhash[language] = 1
  offurl = offurl_hash.get(myid,'None')
  country = country_hash.get(myid,'None')
  place = place_hash.get(myid,'None')
  count += 1
  #print(count)
  #print('https://www.wikidata.org/wiki/' + id)
  title = thishash['title']
  #print(title)
  description = thishash['description']
  #print(description)
  base_url = thishash['claims']['P856']
#  if type(base_url) is list:
  if isinstance(base_url,list):
    base_url = base_url[0]
  base_url2 = thishash['wikidata']['official website (P856)']
#  if type(base_url2) is list:
  if isinstance(base_url2,list):
    base_url2 = base_url2[0]
  if base_url != base_url2:
    #print('Something went wrong')
    #print(base_url)
    #print(base_url2)
    break
  #print(base_url)
  #print(base_url2)
  full_url = base_url + '/wp-json/wp/v2/posts?search='
  #print(full_url)
  #print(offurl)
  print(country)
  print(place)
  this_hash = {}
  this_hash['id'] = myid
  this_hash['title'] = title
  this_hash['base_url'] = base_url
  this_hash['country'] = country
  this_hash['place'] = place
  this_hash['language'] = language
  qidhash[myid] = this_hash
  wordpress_legitimate_list.append(thisfilename)
  #inp = input('press any key to continue')
  print('************')
#outfile = open("outfile_wplegit.txt",'w')
#outfile.write(json.dumps(wordpress_legitimate_list))
#outfile.close
#print(wordpress_legitimate_list)
#langcount = 0
#for i in langhash.keys():
#    print(str(i) + ' | ' + str(langhash[i]))
#    langcount += langhash[i]
#print(langcount)
with open('qidhash.json','w',encoding='utf-8') as myoutfile:
  myoutfile.write(json.dumps(qidhash))
print(qidhash)
