import sys
import re
import nltk
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt
import operator


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return  sorted(unusual)

speaker=sys.argv[1]
c = PlaintextCorpusReader('/Users/juanhuerta/work/NLP_course',speaker+'.txt')
#print c.words('file1.txt')
#print c.sents()
#c.raw()

my_dict={}
for sent in c.sents():
    for word in sent:
        if not word in my_dict:
            my_dict[word]=0
        my_dict[word]+=1
my_dict_sorted=sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)
#print my_dict_sorted


print unusual_words(c.words())
