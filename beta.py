# coding: utf-8
from getimages import get_image , download_image
from makeafact import fact_gen
query = 'lion'
fact = '''10,000 years ago Lions were the second most widespread land mammal, after humans. They existed across Africa, Eurasia and America.'''
url = get_image(query)
download_image(url, query) 

fact_gen(query,fact)
