import os
import json
import re
import requests
import csv

wikidata_query_result_file = open("wikidata_query_result.json",'r')
query_result = json.loads(wikidata_query_result_file.read())

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

legit_file = open("outfile_wplegit.txt",'r')

legit_list = json.loads(legit_file.read())

legit_file.close()

wordpress_legitimate_list = []

count = 0
langhash = {}
print


def fetch_language(id):
  return language_hash[id]

def fetch_offurl(id):
  return offurl_hash.get(id,'None')

def fetch_country(id):
  return country_hash.get(id,'None')

def fetch_place(id):
  return place_hash.get(id,'None')



qidhash = {}
for thisfilename in legit_list:
    thisfile = open('wikidata/' + thisfilename)
    thishash = json.loads(thisfile.read())
    thisfile.close()
    #print(thisfilename)
    id = thishash['wikibase']
    language = thishash['wikidata'].get('language of work or name (P407)','None')
    #print(language)
    #language = thishash['wikidata']['language of work or name (P407)']
    if type(language) is list:
        language = language[0]
    if not language == 'None':
      #print(language)
      if language in list(langhash.keys()):
        langhash[language] += 1
      else:
        langhash[language] = 1
    else:
      language = fetch_language(id)
      #print(language)
      if language in list(langhash.keys()):
        langhash[language] += 1
      else:
        langhash[language] = 1
    offurl = fetch_offurl(id)
    country = fetch_country(id)
    place = fetch_place(id)
    count += 1
    #print(count)
    #print('https://www.wikidata.org/wiki/' + id)
    title = thishash['title']
    #print(title)
    description = thishash['description']
    #print(description)
    base_url = thishash['claims']['P856']
    if type(base_url) is list:
        base_url = base_url[0]
    base_url2 = thishash['wikidata']['official website (P856)']
    if type(base_url2) is list:
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
    this_hash['id'] = id
    this_hash['title'] = title
    this_hash['base_url'] = base_url
    this_hash['country'] = country
    this_hash['place'] = place
    this_hash['language'] = language
    qidhash[id] = this_hash
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
outfile = open("qidhash.json",'w')
outfile.write(json.dumps(qidhash))
outfile.close
print(qidhash)
