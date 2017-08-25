# coding: utf-8
from getimages import get_image , download_image
from cardgenerator import card_gen
query = 'beer'
fact = '''A 'schooner' of beer is really different depending on where you order. In Canada it is always big but in Australia it is usually small.'''
url = get_image(query)
download_image(url, query) 

card_gen(query,fact)
