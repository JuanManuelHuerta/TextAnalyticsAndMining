import sys
import re
import nltk
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt
import operator


def in_a_not_in_b(text_1,text_2):
    text_vocab_1 = set(w.lower() for w in text_1 if w.isalpha())
    text_vocab_2 = set(w.lower() for w in text_2 if w.isalpha())
    unusual = text_vocab_1.difference(text_vocab_2)
    return  sorted(unusual)

speaker=sys.argv[1]
c = PlaintextCorpusReader('/Users/juanhuerta/work/NLP_course',speaker+'.txt')
speaker=sys.argv[2]
d = PlaintextCorpusReader('/Users/juanhuerta/work/NLP_course',speaker+'.txt')
#print c.words('file1.txt')
#print c.sents()
#c.raw()

#my_dict={}
#for sent in c.sents():
#    for word in sent:
#        if not word in my_dict:
#            my_dict[word]=0
#        my_dict[word]+=1
#my_dict_sorted=sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)
#print my_dict_sorted


print in_a_not_in_b(c.words(),d.words())
