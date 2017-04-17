# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from authentication import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,q='#100DaysOfCode').items(25):

    try:
    	print('Tweet by: @' + tweet.user.screen_name)
     	# Retweet tweets as they are found
    	tweet.retweet()
    	print('Retweeted the tweet')
    	# Favorite the tweet
    	tweet.favorite()
    	print('Favorited the tweet')

   		# Follow the user who tweeted
    	if not tweet.user.following:
            # Don't forget to indent
        	tweet.user.follow()
        	print('Followed the user')

    	sleep(20)
    except tweepy.TweepError as e:
	    print(e.reason)

    except StopIteration :
	     break