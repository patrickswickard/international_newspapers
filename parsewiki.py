"""Uhhh...parse wikidata stuff I guess"""
import os
import json
import re
import requests

def validate_json(json_data):
  """Uhhh...validate JSON"""
  try:
    json.loads(json_data)
  except ValueError as err:
    return False
  return True

DIRECTORY = 'wikidata'

valid_json_returned = []
count = 0

for filename in os.listdir(DIRECTORY):
  myfilename = os.path.join(DIRECTORY,filename)
  if os.path.isfile(myfilename):
    count += 1
    print(count)
    with open(myfilename,'r',encoding='utf-8') as myinfile:
      thisfile_hash = json.loads(myinfile.read())
    thisurl = thisfile_hash['claims']['P856'][0]
    REGEX = r"^(https?://.*?)(/|$)"
    result = re.search(REGEX,thisurl)
    this_base_url = result.group(1)
    url_to_try = this_base_url + '/wp-json/wp/v2/posts?search=water'
    print('Trying ' + url_to_try)
    try:
      page = requests.get(url_to_try, timeout=30)
    except:
      print("something screwy happened but don't sweat it")
    if validate_json(page.text):
      print("Valid JSON returned for " + filename)
      valid_json_returned.append(filename)

with open('outfile.txt','w',encoding='utf-8') as myoutfile:
  myoutfile.write(json.dumps(valid_json_returned))
