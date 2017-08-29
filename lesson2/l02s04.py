import sys
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tree import Tree

import os
from nltk.parse import stanford

def traverseTree2(tree):
    current=[]
    #print("tree:", tree)
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            current.append(traverseTree(subtree))
        else:
            current.append((str(subtree[0]),str(subtree[1])))
    return current

def traverseTree(tree):
    current=[]
    #print("tree:", tree)
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            if subtree.height() > 2:
                current.append(traverseTree(subtree))
            else:
                current.append((subtree.label(),str(subtree.flatten())))
        else:
            current.append(subtree)
    return current




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

#http://www.nltk.org/_modules/nltk/tree.html

for x in sents:
    y=parser.raw_parse(x)
    for t in y:
        print "\n\n NEW TREE\n"
        print t
        print "Subtrees of height", int(sys.argv[1])

        for s in t.subtrees(lambda t: t.height() == int(sys.argv[1])):
            print(s)

        print type(t)
        print "++++"
        print traverseTree(t)
        print "-----"
        for i in t.subtrees(filter=lambda x: x.label() == 'NP'):
            print i
        t.draw()
        print "-----"
        print "-----"




