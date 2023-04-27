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

So far, roughly 6000 newspaper websites were identified.  About 1000 of these were determined to be running Wordpress API on the back end available to perform a simple search returning JSON.  Of these, about 862 appeared to be current functional non-spam newspaper websites.

Next steps:

* Write code to explore the metadata for a given set of wikidata objects for possible subsets of interest.

* Using the existing "legitimate newspapers" set, identify subsets of interest (e.g. African newspapers, French language newspapers, etc)

* Create code to search a subset of interest returning some adjustable maximum number of results per source possibly within a date range, etc

* Create code to scrape a subset of interest similar to above (with a query or all articles with a null query)

* "Good citizen" bonus for identifying missing data that can be trivially enhanced in on Wikidata itself.
