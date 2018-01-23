# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:03 2017

@author: Acer
"""
import nltk
from nltk.parse.generate import generate
from nltk import CFG
gram= CFG.fromstring("""
 S -> NP VP
 VP -> V NP | V NP PP
 V -> "saw" | "ate"
 NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
 Det -> "a" | "an" | "the" | "my"
 N -> "dog" | "cat" | "cookie" | "park"|"table"
 PP -> P NP
 P -> "in" | "on" | "by" | "with"
 """)
print(gram)
for sentence in generate(gram, n=13):
    print(' '.join(sentence))
    
for sentence in generate(gram, depth=4):
    print(' '.join(sentence))
    
sentence="Mary saw a cat in the park".split()
rd_parser=nltk.RecursiveDescentParser(gram)
for p in rd_parser.parse(sentence):
    print(p)
   



nltk.data.load('nltk_teach\\examples\\grammars\\book_grammars\\sql0.fcfg')
