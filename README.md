# international_newspapers
Goal will be to do the following:

*  Download information on international newspapers from Wikidata

*  Determine which may be trivially searchable with known backend APIs and allow user to search some subset of them

*  Possibly fill in missing data where appropriate

USAGE:

First 
pip3 install wikidata-dl

then

wikidata-dl get_newspaper_info.sparql


also 
pip3 install mkwikidata

PROGRESS

This mess is currently in the hacking phases and not meant for public use.  Pardon the untidiness.

This methodology could be followed in general for different sets of sites of interest, but in particular the ultimate goal is to identify websites which are searchable and scrapable via Wordpress API.  Wordpress API has a very simple and configurable search, can be presented with a null search to return "all" results (useful for "gentle" scraping), and returns results in a regular and predictable JSON format.  Here's the plan.

* Generate a sparql query that aggregates some data set from wikidata that have associated website urls along with associated metadata of interest.  The initial query here was used to find international newspapers with websites since it is EXTREMELY common for newspaper websites in particular to run Wordpress on their back end.

* Using python's requests library, attempt to search the site using the url prefix with a Wordpress API request and determine if valid JSON which appears to be a Wordpress API response was obtained.

* Once we've narrowed the list to urls that respond to wordpress api, we have a list of candidates for which we can perform a search or scrape.  However, it is likely that a lot of these sites are defunct, semi-functional or dysfunctional, or taken over by spammers.  Therefore at this point human intervention (possibly semi-automated) is required.  Inappropriate sites should be removed from the set so that we are only looking at sites that may be worth searching or scraping.

* The final product of this ends up being a set of wikidata objects with associated urls that can be trivially searched by Wordpress API.  And since these are all Wikidata objects, there is ample metadata for searching some subset or superset of those associated objects.

So far, roughly 6000 newspaper websites were identified.  About 1000 of these were determined to be running Wordpress API on the back end available to perform a simple search returning JSON.  Of these, roughly 860 appeared to be current functional non-spam newspaper websites.

After identifying the legitimate newspapers searchable with Wordpress API, I went through the data available in wikidata corresponding to those newspapers in particular to identify the primary language for each source.  About half of the wikidata items had a P407 (language of work or name) associated with them, hopefully accurate.  For the ones where the P407 field was missing, I did a cleanup job.  I identified the sources that were missing this information and filled those fields in on the Wikidata site when it was possible to do so.  I then re-ran the wikidata query and this allowed me for nearly all the sources to identify the primary language for search and/or translation purposes by combining the results of that search with the data I had previously grabbed.  This was a bit "hacky" but it resulted in more metadata for me and a benefit for other Wikidata users.

Useful files:

get_newspaper_info.sparql - a sparql query for grabbing fields of interest from Wikidata

wikidata_query_result.json - a json dump of as a result of running the sparql query above after cleaning up data as previously described

language_hash.json - a json hash which is keyed on the QID of wikidata items corresponding to newspapers with values corresponding to the language of the newspaper

spam.txt - a list of wikidata file ids downloaded by wikidata-dl corresponding to sites which appear to no longer function as newspapers (e.g. taken over by spammers or squatters, extremely low-quality or dubious sites, etc)

outfile_wplegit.json - json file consisting of a list of json files (format QID.txt) which correspond to legitimate-seeming newspaper sites and containing information from Wikidata on those sites

Note that a lot of this code is a bit hacky.  Part of the reason for this is that some of the tools and modules I've been using to grab information from Wikidata such as wikidata-dl, while useful, have a lot of frustrating bugs and quirks and different functionality between versions.

Next steps:

* Immediate next step: need a static json file that is keyed on each legitimate newspaper item QID and has at minimum the information given in the big SPARQL query that got spit out to wikidata_query_result.json .

* After that step, flesh out other fields from the spotty information "accidentally" downloaded with wikidata-dl tool.  (Not all items download due to some bugs, but this contains more complete information than is given from the regular SPARQL query)

* Need code that can load the information from a legitimate hash and perform a search given as input a QID and a search query and save/display the data for the user.  The basics of performing this search will be fairly straightforward

* Write code to explore the metadata for a given set of wikidata objects for possible subsets of interest.

* Using the existing "legitimate newspapers" set, identify subsets of interest (e.g. African newspapers, French language newspapers, etc)

* Create code to search a subset of interest returning some adjustable maximum number of results per source possibly within a date range, etc

* Create code to scrape a subset of interest similar to above (with a query or all articles with a null query)

* "Good citizen" bonus for identifying missing data that can be trivially enhanced in on Wikidata itself.  Currently doing this for >400 wikidata entries for valid newspapers that lack information about which language is used (P407).

Horizon:

* Useful uses for this include as above creating an instantly-searchable set of endpoints or a means to create repositories of sets of text for analysis from various news sources

* Playful uses for this could combine other fun and useless scripts such as hunting for accidental haikus, etc.
