# twitter-search
Searches Twitter for given hashtag

coronavirus.py generates a dataset of tweets containing specified search term.

datacollection.py runs coronavirus.py for each element in list of search terms. 


Instructions:

A 'credentials.json' file with your Twitter API credentials is required at the top level of the twitter-search directory (alongside coronavirus.py and datacollection.py)
 
Format credentials.json like this:

{
\
&nbsp;&nbsp;&nbsp;&nbsp;"consumer_key" : "your consumer key",
	\
&nbsp;&nbsp;&nbsp;&nbsp;"consumer_secret" : "your consumer secret",
	\
&nbsp;&nbsp;&nbsp;&nbsp;"access_token" : "your access token",
	\
&nbsp;&nbsp;&nbsp;&nbsp;"access_token_secret" : "your access token secret"
	\
}


Then run:

`python3 datacollection.py`

to begin the program. Terminate the program with CTRL-C or CTRL-Z (OS Specific).
