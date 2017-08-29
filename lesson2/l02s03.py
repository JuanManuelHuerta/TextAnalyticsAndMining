import sys
from bs4 import BeautifulSoup
import re
import nltk


import os
from nltk.parse import stanford




os.environ['STANFORD_PARSER'] = '/Users/juanhuerta/work/NLP_course/lesson2/stanford-parser-full-2015-12-09/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/Users/juanhuerta/work/NLP_course/lesson2/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'

parser = stanford.StanfordParser(model_path="/Users/juanhuerta/work/NLP_course/lesson2/stanford-parser-full-2015-12-09/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

fp=open("obama-convention.html","rt")
html_doc=fp.read()
od = BeautifulSoup(html_doc, 'html.parser')

inline_content =od.find('article', attrs={'itemprop':'articleBody'})  
my_corpus=  inline_content.text

cleaned_up = re.sub(r'\([A-Z\s]+\)','',my_corpus)
#print cleaned_up

sents= nltk.tokenize.sent_tokenize(cleaned_up)[90:100]
sps=parser.raw_parse_sents(sents)
for x in sps:
        for y in x:
            y.draw()


'''
sentences = parser.raw_parse_sents(("Hello class, this is a parse tree.", "The goal of the class is to learn to extract information from text"))
print sentences

# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()

'''

