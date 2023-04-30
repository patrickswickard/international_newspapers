import os
import json
import re
import requests
import csv
import pandas

wikidata_query_result_file = open("full_list_of_businesses.json",'r')
query_result = json.loads(wikidata_query_result_file.read())

list_of_what_we_care_about = []

query_list = query_result['results']['bindings']
country_count_hash = {}

for item in query_list:
  id1 = item.get('item',{}).get('value')
  id_clean = re.sub('http://www.wikidata.org/entity/','',id1)
  offurl = item.get('offurl',{}).get('value')
  country = item.get('countryLabel',{}).get('value')
  simplehash = {}
  simplehash['id'] = id_clean
  simplehash['offurl'] = offurl
  simplehash['country'] = country
  list_of_what_we_care_about.append(simplehash)
  # this is better done in pandas but here's a DIY
  if country in list(country_count_hash.keys()):
    country_count_hash[country] += 1
  else:
    country_count_hash[country] = 1

# Pandas does some automatic exploration and processing

df = pandas.DataFrame(list_of_what_we_care_about)
print('***********************')
print(df)
print('***********************')
print(df.describe())
print('***********************')
print(df.dtypes)
print('***********************')
print(df.info())
print('***********************')
print(df['country'])
print('***********************')
print(df['country'].value_counts().to_string())
