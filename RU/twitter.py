
print('Importando tweepy')
import tweepy

print('Importando chaves')
from twitter_keys import *

def post (text):
	print('Autenticando....')
	client = tweepy.Client(
	#	bearer_token = bearer_token,
		consumer_key = consumer_key, 
		consumer_secret = consumer_secret,
		access_token = access_token, 
		access_token_secret = access_token_secret
	)

	print('Postando', text)
	t = client.create_tweet(text=text)

	print(t)
	print('\n', dir(t))

	print('\n\n', t.data['id'])
	print('\t', t.data['text'])

print('Twitter carregado com sucesso!')