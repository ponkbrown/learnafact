# coding: utf-8
import os
from getimages import download_image
from cardgenerator import card_gen
from hello_db import db, Fact
from apis import reddit, unsplash
from datetime import datetime
from textblob import TextBlob
import random
import webbrowser

# This create a dir data to store all the variables needed to fill the db
data = { 'name' :'', 'date' : '', 'fact': '', 'fact_img':'', 'url' : '', 'img_id' : '', 'reddit_id' : '', 'published' : False }


# Get a random submision from /r/todayilearned subreddit
til = reddit.subreddit('todayilearned')
subm = til.random()

# extract the title from the sumbision
text = str(subm.title).lower()


# make text a fact text 
if text.startswith(('til that', 'til of')):
    text = text.split()[2:]
    text[0] = text[0].capitalize()
    text = ' '.join(text)
    
elif text.startswith('til'):
    text = text.split()[1:]
    text[0] = text[0].capitalize()
    text = ' '.join(text)

# Getting nouns to search for an image
textblob = TextBlob(text)
names = []
for pname,tag in textblob.tags:
    if tag.startswith('NN'):
        names.append(pname)

# shuffling the names list and searching for an image in unsplash
random.shuffle(names)
for name in names:
    fotos = unsplash.photos().search_photos(
    query = name,
    per_page=20
    )['results']
    if len(fotos) == 0:
        continue
    foto = random.choice(fotos)
    break

# Download the image selected
image = download_image(foto['urls']['regular'], name)

# Generate a card fact
card = card_gen(image, name, text)

# Borra la imagen descargada
os.remove(image)

data['name'] = name
data['date'] = datetime.now()
data['fact'] = text
data['fact_img'] = ''
data['url'] = subm.url
data['reddit_id'] = subm.id
data['img_id'] = foto['id']

fact = Fact(**data)
db.session.add(fact)
db.session.commit()


try:
    webbrowser.open(card['fact_img'])
except:
    pass
