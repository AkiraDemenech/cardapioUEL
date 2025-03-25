
import atproto

from bsky_keys import *

client = atproto.Client()
client.login(
	handle, password
)

text = 'Hello, world!'
t = client.send_post(text=text)

print(t)
print('\n', dir(t))

