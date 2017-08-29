import sys
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tree import Tree

import os


fp=open("obama-convention.html","rt")
html_doc=fp.read()
od = BeautifulSoup(html_doc, 'html.parser')

inline_content =od.find('article', attrs={'itemprop':'articleBody'})  
my_corpus=  inline_content.text

cleaned_up = re.sub(r'\([A-Z\s]+\)','',my_corpus)
#print cleaned_up

sents= nltk.tokenize.sent_tokenize(cleaned_up)

#http://www.nltk.org/_modules/nltk/tree.html

for x in sents:
    print x
    #y=[z[1] for z in nltk.pos_tag(nltk.word_tokenize(x))]
    #print y
    y=nltk.pos_tag(nltk.word_tokenize(x))
    for i in range(len(y)-1):
        if y[i][1]=='JJ' and y[i+1][1]=='NN':
            print y[i], y[i+1]
