
import requests
import re 

URL = 'https://sites.uel.br/sebec/cardapio/'

def texto (html):
	b = s = None
	n = False 
	l = []
	t = [(n, l)]

	for c in html:
		if s: # se está em modo de string
			if c == s and b != '\\': # fecha string 
				s = None # não está mais em modo de string
			continue	# ignora tudo 

		if c == '<': # abre tag
			n += 1 # próximo nível 
			l = []
			t.append((n, l))			
		elif c == '>': # fecha tag 	
			if n > 0: # se estiver em alguma tag
				n -= 1 # nível anterior
		elif n: # numa tag
			if c in '"\'': # entra em modo string
				s = c # considera o tipo certo de aspas
		else: # fora de uma tag	
			l.append(c)

#	return t
	return [
		(nv, ''.join(ln))#.strip()
		for nv, ln in t
	]		

def acessar (url = URL):
	r = requests.get(url)
	print(r)
	print(len(r.content))	
	return r.content.decode()

def cardapio (texto):  
	dias = {}
	dia = []

	for nv, ln in texto:		
		if ln.isspace() or not len(ln):
			continue 
		if '!' in ln: # fim do cardápio no bom final de semana!
			dia = []
		#	print(ln)

		d = re.search(r'((?:\d+/)+\d+)', ln)	
		if d:
			data = tuple(int(num) for num in d.groups()[0].split('/'))
			print('\n',data)
			if data in dias: 
				print('continua')
				dia = dias[data]
			else:	
				dias[data] = dia = []

		dia.append(ln.strip().split())		
	return dias		

#print(cardapio(texto(acessar())))