'''Connect to Twitter API'''
import tweepy
import csv

consumer_key = 'zLoTyTpJ9rHIVdTd3ZtI5YUSp'
consumer_secret = '9LszIWxvxL5vPfzCvIsWglXyDmqWiip0N94upSx3a7swg3Xl1H'
access_token = '1068395390909771776-HCxIyBND3cHYPh87JETdr00tAPB9D4'
access_token_secret = 'mHQp7o8xZo6XOQHlInSlZeLildpNZSkG4NuE0R6nuXPql'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

with open('data/CoronaVirusUpdate.csv', 'w') as f:
	writer = csv.writer(f, dialect='excel')

	labels = ["id", "date", "user", "text", "retweet_count", "favorite_count", "location"]
	writer.writerow(labels)

	maxid = 0
	public_tweets = api.search("#CoronaVirusUpdate", lang = 'en', count = 100)

	for tweet in public_tweets:
		if 'RT @' not in tweet.text and '=@' not in tweet.text:
			writer.writerow([tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text,
							tweet.retweet_count, tweet.favorite_count, tweet.user.location])
			if maxid == 0 or tweet.id < maxid:
				maxid = tweet.id

	for i in range(50):
		public_tweets = api.search("#CoronaVirusUpdate", lang = 'en', count = 100, max_id=ms)
		for tweet in public_tweets:
			if 'RT @' not in tweet.text and '=@' not in tweet.text:
				writer.writerow([tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text,
								tweet.retweet_count, tweet.favorite_count, tweet.user.location])
				if tweet.id < maxid:
					maxid = tweet.id
