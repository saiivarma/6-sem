# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:26:00 2017

@author: Acer
"""

from nltk.corpus import wordnet as wn
wn.synsets('motorcar')  # Synonym for the word 'motorcar'
 
 
for synset in wn.synsets('car'):
    for lemma in synset.lemmas():
        print(lemma.name())
        
for synset in wn.synsets('dog'):
    for lemma in synset.lemmas():
        print(lemma.name())
        

for synset in wn.synsets('Machine'):
    for lemma in synset.lemmas():
        print(lemma.name())
        
                
for synset in wn.synsets('Happy'):
    for lemma in synset.lemmas():
        print(lemma.name())
        

wn.synset('car.n.01').lemmas()
wn.synset('machine.n.01').lemmas()


wn.synset('car.n.01').definition()

wn.synset('car.n.01').examples()

for synset in wn.synsets('motorcar'):
    for lemma in synset.lemmas():
        print(lemma.name())
        
        
for synset in wn.synsets('machine'):
    print(synset.lemmas(), synset.definition(), '\n')
    
for synset in wn.synsets('dish'):
    print(synset.lemmas(), synset.definition(), synset.examples(),'\n')
