import os
import json
import re
import requests

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

directory = 'wikidata'

valid_json_returned = []
count = 0

for filename in os.listdir(directory):
    f = os.path.join(directory,filename)
    if os.path.isfile(f):
        count += 1
        print(count)
        thisfile = open(f)
        thisfile_hash = json.loads(thisfile.read())
        thisfile.close()
        thisurl = thisfile_hash['claims']['P856'][0]
        regex = r"^(https?://.*?)(/|$)"
        result = re.search(regex,thisurl)
        this_base_url = result.group(1)
        url_to_try = this_base_url + '/wp-json/wp/v2/posts?search=water'
        print('Trying ' + url_to_try)
        try:
          page = requests.get(url_to_try, timeout=30)
        except:
          print("something screwy happened but don't sweat it")
        if validateJSON(page.text):
          print("Valid JSON returned for " + filename)
          valid_json_returned.append(filename)

outfile = open("outfile.txt",'w')
outfile.write(json.dumps(valid_json_returned))
outfile.close
