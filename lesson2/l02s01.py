import sys
from bs4 import BeautifulSoup
import re
import nltk



fp=open("obama-convention.html","rt")
html_doc=fp.read()
od = BeautifulSoup(html_doc, 'html.parser')

inline_content =od.find('article', attrs={'itemprop':'articleBody'})  
my_corpus=  inline_content.text

cleaned_up = re.sub(r'\([A-Z\s]+\)','',my_corpus)
print cleaned_up



