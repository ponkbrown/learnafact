# coding: utf-8
import argparse
from factos import getfacts
from getimages import get_image, download_image
from cardgenerator import card_gen
import pdb

def carding(fact):
    ''' Shows the fact and prompt for theme for an image'''
    query = input('Image theme:')
    image_url = get_image(query)
    if image_url == 0:
        print("not apropiate image was found, sorry.")
        exit()
    else:
        download_image(image_url, query)
        card_gen(query, fact)

    print(query)
    
# Creando el menu para la linea de comandos
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=int, default=1, help='Number of facts to display')
parser.add_argument('-i', action='store_true', help='add an [IMAGE] to the selected fact (It promps for a picture theme)')

args = parser.parse_args()

# Generando el numero de facts
facts = getfacts(args.f)


fact_number = 0
count = 0
for fact in facts:
    count += 1
    print('[{}]\nfact: {}\n url: {}\n reddit_id: {}\n'.format(count,fact[0],fact[1], fact[2]))

if args.i:
    if args.f > 1:
        fact_number = int(input('Select Fact Number [{}] to [{}]: '.format(1,len(facts))))
        fact = facts[fact_number-1]
        
    print('\n\n'+fact[0]+'\n')
    input('Press Enter to Continue')
    carding(fact[0])
