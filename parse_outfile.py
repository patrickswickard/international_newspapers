"""Attempts searches and keeps track of valid/invalid, I think"""
import json
import requests

with open('outfile.txt','r',encoding='utf-8') as myinfile:
  outlist = json.loads(myinfile.read())

unresponsive_list = []
wordpress_site_list = []
wordpress_nonsite_list = []

count = 0
for thisfilename in outlist:
  count += 1
  print(count)
#  thisfile = open('wikidata/' + thisfilename)
#  thishash = json.loads(thisfile.read())
#  thisfile.close()
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
  try:
    result = requests.get(full_url,timeout=20)
    page_text = result.text
  except:
    print('something went wrong with request')
    unresponsive_list.append(thisfilename)
    continue
  #print(page_text)
  try:
    this_result_list = json.loads(page_text)
    if this_result_list:
      if this_result_list[0]['id']:
        print('Looks like Wordpress to me!')
        wordpress_site_list.append(thisfilename)
        continue
  except:
    print('something went wrong parsing json')
    wordpress_nonsite_list.append(thisfilename)
    continue
  print('************')

with open('outfile_wpconfirmed.txt','w',encoding='utf-8') as myoutfile:
  myoutfile.write(json.dumps(wordpress_site_list))
with open('outfile_wpunconfirmed.txt','w',encoding='utf-8') as myoutfile:
  myoutfile.write(json.dumps(wordpress_nonsite_list))
with open('outfile_unresponsive.txt','w',encoding='utf-8') as myoutfile:
  myoutfile.write(json.dumps(unresponsive_list))
