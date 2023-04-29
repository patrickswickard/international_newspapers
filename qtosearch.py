import os
import json
import re
import requests
import csv

qidfile = open("qidhash.json",'r')
qidhash = json.loads(qidfile.read())

thisqidlist = []
for qid in list(qidhash.keys()):
    language = qidhash.get(qid).get('language')
    print(language)
    if language == 'French (Q150)':
      thisqidlist.append(qid)

#thisqidlist = ['Q16979942']

article_list = []

for thisqid in thisqidlist:
  this_base_url = qidhash[thisqid]['base_url']
  this_query = 'eau'
  rpp = '10' # 100 works but kinda big
  order_by = 'date'
  order = 'desc'
  this_request_url = this_base_url + '/wp-json/wp/v2/posts?search=' + this_query + '&per_page=' + rpp + '&orderby=' + order_by + '&order=' + order
  #print(this_request_url)
  #print(this_base_url)
  print(this_query)
  try:
    result = requests.get(this_request_url,timeout=20)
    article_hash = json.loads(result.text)
  except:
    continue

  for this_article in article_hash:
    title = this_article.get('title',{}).get('rendered')
    article_link = this_article.get('link',{})
    content = this_article.get('content',{}).get('rendered')
    print(title)
    #print(article_link)
#    print(content)
    article_list.append(this_article)

outfile = open("french_source_eau_search.json",'w')
outfile.write(json.dumps(article_list))
outfile.close
