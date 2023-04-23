import os
import json
import re
import requests

confirmed_file = open("outfile_wpconfirmed.txt",'r')

confirmed_list = json.loads(confirmed_file.read())

confirmed_file.close()

#unresponsive_list = []
#wordpress_site_list = []
#wordpress_nonsite_list = []

count = 299
for thisfilename in confirmed_list[299:100000]:
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
    base_url = thishash['claims']['P856'][0]
    print(base_url)
    full_url = base_url + '/wp-json/wp/v2/posts?search='
    print(full_url)
    inp = input('press any key to continue')
#    try:
#      result = requests.get(full_url,timeout=20)
#      page_text = result.text
#    except:
#      print('something went wrong with request')
#      unresponsive_list.append(thisfilename)
#      continue
#    #print(page_text)
#    try:
#      this_result_list = json.loads(page_text)
#      if this_result_list:
#        if this_result_list[0]['id']:
#          print('Looks like Wordpress to me!')
#          wordpress_site_list.append(thisfilename)
#          continue
#    except:
#      print('something went wrong parsing json')
#      wordpress_nonsite_list.append(thisfilename)
#      continue
    print('************')
     
#outfile = open("outfile_wpconfirmed.txt",'w')
#outfile.write(json.dumps(wordpress_site_list))
#outfile.close
#outfile = open("outfile_wpunconfirmed.txt",'w')
#outfile.write(json.dumps(wordpress_nonsite_list))
#outfile.close
#outfile = open("outfile_unresponsive.txt",'w')
#outfile.write(json.dumps(unresponsive_list))
#outfile.close
