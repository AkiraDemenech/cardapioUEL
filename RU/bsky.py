
print('Importando atproto')
import atproto

print('Importando chaves')
from bsky_keys import *

def post (text):
	print('Autenticando....')
	client = atproto.Client()
	client.login(
		handle, password
	)

	print('Postando', text)
	t = client.send_post(text=text)

	print(t)
	print('\n', dir(t))

	print('\n\n', t.uri)
	print('\t', t.cid)

print('Bluesky carregado com sucesso!')
