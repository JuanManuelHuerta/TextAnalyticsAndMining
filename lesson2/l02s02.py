import sys
from bs4 import BeautifulSoup
import re
import nltk


import os
from nltk.parse import stanford




os.environ['STANFORD_PARSER'] = '/Users/juanhuerta/work/NLP_course/lesson2/stanford-parser-full-2015-12-09/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/Users/juanhuerta/work/NLP_course/lesson2/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'

parser = stanford.StanfordParser(model_path="/Users/juanhuerta/work/NLP_course/lesson2/stanford-parser-full-2015-12-09/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
sentences = parser.raw_parse_sents(("Hello class, this is a parse tree.", "The goal of the class is to learn to extract information from text"))
print sentences

# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()






