import sys
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tree import Tree

import os
from nltk.parse import stanford

#### Im losing the label of the subtree as I recursively traverse the tree, only leafs will keep label

def traverseTree(tree):
    #print "Im here", tree, tree.height(), tree.label(), str(tree.flatten())
    current=[]
    #print("tree:", tree)
    if tree.height()==2:
        current.append([str(tree.flatten())])
    else:
        for subtree in tree:
            if subtree.height() > 2:
                current.append(traverseTree(subtree))
            else:
                current.append([str(subtree.flatten())])
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
    print "-----New Sentence-----"
    y=parser.raw_parse(x)
    for t in y:
        #print t
        print "    --- new subtree -----"
        #for s in t.subtrees(lambda t: (t.height() >= 3 and t.label() =='NP')):
        for s in t.subtrees(lambda t: (t.height() >= 3 and t.label() ==sys.argv[1])):
            print "This is a subtree structure:"
            print(s)
            print "This is as embedded lists:"
            print traverseTree(s)
            print "\n"
        #print type(t)



