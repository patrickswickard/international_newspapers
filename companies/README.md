This is a larger and simpler example of the process used for the newspapers

fetch_business.py contains a sparql query through mkwikidata to fetch all businesses which have an official url (offurl) and country (country) set.  Note this has a pretty good probability of timing out the first time (which will raise an error when we try to parse json) but retrying usually works.

full_list_of_businesses.json  is the file this query gets dumped to.  From there we can work "offline" without further querying wikidata.

process_full_list_of_businesses.json helps us explore the metadata "offline" from what we grabbed before.
