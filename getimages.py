# coding: utf-8
import requests
import shutil
import random
from apis import unsplash


def get_image(query):
    ''' Busca en unsplash imagenes de [query] selecciona una aleatoria y devuelve la url de la imagen '''

    fotos = unsplash.photos().search_photos(
    query = query,
    page=1,
    per_page=20
    )
    
    if 'results' in fotos:
        results= fotos['results']
    # Si no encuentra nada la busqueda regresa 0
    if not results:
        return 0

    foto = results[random.randint(0,len(results)-1)]
    user = foto['user']
    url = foto['urls']['regular']
    return url


def download_image(url, filename):
    ''' recibe una [url] y la guarda como ./images/[filename].jpg '''

    response = requests.get(url, stream=True)
    with open('./images/'+filename+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return ('./images/' + filename + '.jpg')

