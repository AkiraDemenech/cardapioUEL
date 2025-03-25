
import tweepy

from twitter_keys import *

client = tweepy.Client(
#	bearer_token = bearer_token,
	consumer_key = consumer_key, 
	consumer_secret = consumer_secret,
	access_token = access_token, 
	access_token_secret = access_token_secret
)

text = 'Olá, mundo!'
t = client.create_tweet(text=text)

print(t)
print('\n', dir(t))

