import os
import json
import re
import requests
import csv

qidfile = open("qidhash.json",'r')
qidhash = json.loads(qidfile.read())


thisqid = 'Q5352174'

this_base_url = qidhash[thisqid]['base_url']
this_query = 'agua'
this_request_url = this_base_url + '/wp-json/wp/v2/posts?search=' + this_query

print(this_base_url)
print(this_query)
result = requests.get(this_request_url,timeout=20)

print(result.text)
