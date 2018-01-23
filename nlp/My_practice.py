# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:13:04 2017

@author: Acer
"""

import nltk
import string
from nltk.corpus import stopwords
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
grammar = CFG.fromstring(demo_grammar)
print(grammar)
for sentence in generate(grammar, n=13):
    print(' '.join(sentence))
    
for sentence in generate(grammar, depth=4):
    print(' '.join(sentence))
    
len(list(generate(grammar, depth=3)))

len(list(generate(grammar, depth=4)))

len(list(generate(grammar, depth=5)))

len(list(generate(grammar, depth=6)))

len(list(generate(grammar, depth=7)))

list(generate(grammar, depth=5))

print(stopwords.words('english')[0:100])

test_sentence="Hello Mani, How are you doing this today? Let me tell you one thing, what had happend earlier, not necessarily will happen again. It entirely depends on the situation"

tokens=nltk.word_tokenize(test_sentence)

print(tokens)

no_punctuation=[char for char in test_sentence if char not in string.punctuation]
print(no_punctuation)

no_punctuation=''.join(no_punctuation)
print(no_punctuation)

allwords=no_punctuation.split()
print(allwords)

clean_sentance=[word for word in allwords if word.lower() not in stopwords.words('english')]

print(clean_sentance)