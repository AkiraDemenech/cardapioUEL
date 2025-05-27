#!/usr/bin/env python3

arquivo = 'leitura.log'
post = 'post.log'

print('Importando....')
import time 
import uel 
import sys

import twitter
import bsky

if len(sys.argv) > 1:
	arquivo = sys.argv[1]
if len(sys.argv) > 2:
	post = sys.argv[2]	

try:
	print('Lendo do arquivo', arquivo)
	a = uel.cardapio((0, ln) for ln in open(arquivo, 'r'))
except FileNotFoundError:	
	print(arquivo, 'ainda não existente')
	a = {}	

try:
	print('Lendo da web....')
	web = uel.acessar() 

	print('Lendo texto....')
	t = uel.texto(web)

	print('Lendo cardápio....')
	c = uel.cardapio(t)
except:	
	print('Erro na leitura online, utilizando a última leitura registrada')
	c = {}
print(c)
if len(c): 	
	print(a)
else:	
	print('Cardápio vazio!', len(a))
	c = {	# cópia de a
		d: list(a[d])
		for d in a
	}

arq = open(arquivo, 'w')
for d in c:
	print('\n',*d)	
	print(file=arq)

	b = []
	if d in a:
		b = a[d]
	a[d] = False # se não há nenhuma diferença desde a última leitura

	for p in c[d]:
		m = '+'
		if p in b: # já estava na versão anterior
			m = '' 
			b.remove(p)
		else:	
			a[d] = True # registra que houve diferença nesse dia 

		print(m, '\t', *p)
		print(*p, file=arq)
	for p in b:	
		print('-\t', *p)
		a[d] = True # registra a diferença do dia
	
t = time.localtime()[:6]
hoje = tuple(t[:3][::-1])

print('\nHoje é',*hoje)
print('\n!', *t, file=arq)	

if hoje in c:
	print('Hoje tem:')

	texto = '\n'.join(ln[0].upper() + ln[1:].lower() for ln in [' '.join(p) for p in c[hoje]])
	print(repr(texto))
	print(texto)
	
	separador = '!\t'
	redes = anterior = ''

	try:
		print('Lendo post anterior no arquivo',post)
		anterior = open(post, 'r').read()					
	except:	
		print('Não foi possível resgatar registro do último post no arquivo',post)
		
	registro = open(post, 'w')					
	print(repr(anterior))
	
	if separador in anterior:
		redes, anterior = anterior.split(separador, 1)
	print(anterior)		
	print(redes)
	
	for r, post in {
		('Bluesky', bsky.post),
		('Twitter', twitter.post)
	}:				
		if r in redes and anterior == texto:
			print('Já postado no',r)
		else:	
		
			print('Postando no',r,'....')	

			try:
				post(texto)
			 		
			except:
				print('Falha ao postar no ',r,'!') 	 
				r = ''
			
		print(r, file=registro)	
		
	print(separador, end=texto, file=registro) 	
	registro = None
else:
	print('Nenhum cardápio para hoje')
		
print('Bom final de programa!')		
