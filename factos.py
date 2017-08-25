# coding: utf-8
import shelve
import random

d = shelve.open('submisions')
factos = d['subs']
d.close()

def facts(num):
    ''' Regresa una lista con tuplas ( fact, url, reddit_id) '''
    lista = []
    for five in range(num):

        fact = random.choice(factos)
        titulo = fact.title
        lt = titulo.lower()
        
        # estos if son para que se pueda leer com un fact
        if lt.startswith(('til that', 'til of')):
            titulo = titulo.split()[2:]
            titulo[0] = titulo[0].capitalize()
            titulo = ' '.join(titulo)
            
        elif lt.startswith('til'):
            titulo = titulo.split()[1:]
            titulo[0] = titulo[0].capitalize()
            titulo = ' '.join(titulo)

        lista.append((titulo, fact.url, fact.id)) 

    return lista

