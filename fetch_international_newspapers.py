import mkwikidata
import json

# This is a query to select wikidata items that are an "instance of" (P31) "newspaper" (Q11032)
# written so that the items are obliged to have an "official website" (P154)
# along with optional fields "country" (P17) "place of publication" (P291) "language of work or name" (P407)
# and "logo image" (P154)

# The structure of this query should make it clear how this can be modified to include
# other required or optional fields
# For further SPARQL syntax see https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial

query = """
SELECT ?item ?itemLabel ?country ?countryLabel ?place ?placeLabel ?language ?languageLabel ?pic ?offurl
WHERE
{
?item wdt:P31 wd:Q11032 .
OPTIONAL {?item wdt:P17 ?country .}
OPTIONAL {?item wdt:P291 ?place .}
OPTIONAL {?item wdt:P407 ?language .}
OPTIONAL {?item wdt:P154 ?pic .}
?item wdt:P856 ?offurl
SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
}
"""
query_result = mkwikidata.run_query(query, params={ })
#print(query_result)
outfile = open("full_list_of_newspapers.json",'w')
outfile.write(json.dumps(query_result))
outfile.close

