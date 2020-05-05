# -*- coding: utf-8 -*-
"""
Spyder Editor

#This is a temporary script

#
"""
from spacy.lang.en.stop_words import STOP_WORDS
import collections as c

data = open('E:\learning\\Python for DS\\word_count\\98-0.txt', encoding="utf8")
stop_words = list(set(line.strip() for line in open('E:\learning\\Python for DS\\word_count\\stopwords')))
word_count = {}

for r in data.read().lower().split(): 
    r = r.replace(".","")
    r = r.replace(",","")
    r = r.replace("\"","")
    r = r.replace("“","")
    if not r in STOP_WORDS: 
        if r not in word_count:
            word_count[r] = 1
        else:
            word_count[r] += 1

d = c.Counter(word_count)

for word, count in d.most_common(10):
	print(word, ": ", count)