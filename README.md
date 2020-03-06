# twitter-search
Searches Twitter for given hashtag

coronavirus.py generates a dataset of tweets containing specified search term.

datacollection.py runs coronavirus.py for each element in list of search terms. 


Instructions:

A 'credentials.json' file with your Twitter API credentials is required at the top level of the twitter-search directory. 
 
Format credentials.json like this:

{
\
\	"consumer_key" : "your consumer key",
	\
	"consumer_secret" : "your consumer secret",
	\
\	"access_token" : "your access token",
	\
\	"access_token_secret" : "your access token secret"
	\
}


Then run:

`python3 datacollection.py`

to begin the program. Terminate the program with CTRL-C or CTRL-Z (OS Specific).
