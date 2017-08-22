# coding: utf-8
from rake_nltk import Rake
r = Rake()
mytext = '''"Ethiopia Skate", a non-profit org., helped raise money to pay for skateboards for kids in Ethiopia and even created Ethiopia's first skate park in 2016; it's free of charge.'''
r.extract_keywords_from_text(mytext)
r.get_ranked_phrases()
