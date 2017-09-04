# coding: utf-8
import shelve
import random

# carga los facts que estan grabados en submisions.db son facts generados con la biblioteca praw
# las credenciales en el archivo redditrobot.py

# Carga los facts de el archivo submision.db
d = shelve.open('submisions')
factos = d['subs']
d.close()

def getfacts(num):
    ''' Regresa una lista con [num] de tuplas ( fact, url, reddit_id) '''
    lista = []
    for five in range(num):

        fact = random.choice(factos)
        titulo = fact.title
        lt = titulo.lower()
        
        # estos if son para que se pueda leer como un fact
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

