# coding: utf-8
import requests
import shutil
import random
from unsplash_python.unsplash import Unsplash

unsplash = Unsplash({
'application_id': '69b0c91f6bf07c884abc70d0f482fb3d6c84344e5945f0fd89e5693da03699da',
'secret': '84f05ed54863c4e2f44107f39f875a005c70cfb38ecbcc70dc16f533e197d41384f05ed54863c4e2f44107f39f875a005c70cfb38ecbcc70dc16f533e197d413',
'callback_url': 'urn:ietf:wg:oauth:2.0:oob'
})

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
    ''' recibe una [url] y la guarda como [filename].jpg '''

    response = requests.get(url, stream=True)
    with open('./images/'+filename+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return True
