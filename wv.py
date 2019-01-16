#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:21:09 2019

@author: benjaminwasserman
"""

from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

full_book = ""
all_words = []
nested_sent = []
indices = []
no_punc = []
final = []

infile = open("hp1.txt", "rb")
a = infile.readlines()
for i in a:
        new_line = i.decode("utf-8", "ignore")
        #full_book += new_line
        all_words += (new_line.split())

      
for word in all_words:
    word = word.lower()
    word = word.replace(",", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    no_punc.append(word)
        

for i in range(len(no_punc)):
    curr_word = no_punc[i]
    try:
        if curr_word[-1] is ".":
            indices.append(i)
    except IndexError:
        pass
        

for i in range(len(indices)-1):
    nested_sent.append(no_punc[indices[i]+1:indices[i+1]+1])
    

# build vocabulary and train model
model = Word2Vec(
        nested_sent,
        min_count=1,
        workers=8)


model.train(nested_sent, total_examples=len(nested_sent), epochs=10)

words = list(model.wv.vocab)

w1 = ["harry"]        

result = model.most_similar(positive=['harry'], negative=['happy'], topn=3)
print(result)

        