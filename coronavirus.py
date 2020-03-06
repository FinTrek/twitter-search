'''Connect to Twitter API'''
import tweepy
import csv
import json

def authTwitter():
	with open('credentials.json', 'r') as f:
		creds_json = f.read()

	creds = json.loads(creds_json)
	
	consumer_key = creds['consumer_key']
	consumer_secret = creds['consumer_secret']
	access_token = creds['access_token']
	access_token_secret = creds['access_token_secret']

	print('Authorizing Twitter API access... ', end='')
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	print('Done.')
	return api


api = authTwitter()	#Automatically called when imported in other files.

def generateData(phrase, fileCount):
	filename = "data/{}_{}.csv".format(phrase, fileCount)
	with open(filename, 'w') as f:
		writer = csv.writer(f, dialect='excel')

		labels = ["id", "date", "user", "text", "retweet_count", "favorite_count", "location"]
		writer.writerow(labels)

		maxid = 0
		public_tweets = api.search("#{}".format(phrase), lang = 'en', count = 100)

		for tweet in public_tweets:
			if 'RT @' not in tweet.text and '=@' not in tweet.text:
				writer.writerow([tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text,
								tweet.retweet_count, tweet.favorite_count, tweet.user.location])
				if maxid == 0 or tweet.id < maxid:
					maxid = tweet.id

		for i in range(50):
			public_tweets = api.search("#{}".format(phrase), lang = 'en', count = 100, max_id=maxid)
			for tweet in public_tweets:
				if 'RT @' not in tweet.text and '=@' not in tweet.text:
					writer.writerow([tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text,
									tweet.retweet_count, tweet.favorite_count, tweet.user.location])
					if tweet.id < maxid:
						maxid = tweet.id
