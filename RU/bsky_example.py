
print('Importando atproto')
import atproto

print('Importando chaves')
from bsky_keys import *

print('Autenticando....')
client = atproto.Client()
client.login(
	handle, password
)

text = 'Hello, world!'
print('Postando', text)
t = client.send_post(text=text)

print(t)
print('\n', dir(t))

print('\n\n', t.uri)
print('\t', t.cid)
