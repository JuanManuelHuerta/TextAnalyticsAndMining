import sys
from bs4 import BeautifulSoup
import re

fp=open("dead_poets.html","rt")
html_doc=fp.read()
dps = BeautifulSoup(html_doc, 'html.parser')
#print(dps.prettify())

# Beautiful soup
i=0
my_document={}
current_blank=False
current_speaker=""
for line in str(dps.pre).split("\n"):
    i+=1
    ## identify blank lines
    if re.match(r"^\s+$",line):
        current_blank=True
    else:        
        if current_blank==True and re.match(r"^\s+[A-Z0-9\.\s]+\s+$",line):
            current_speaker=line.rstrip().replace(" ","")
            current_blank=False
            continue
            #print current_speaker
        else:
            if  current_speaker!="":
                if not current_speaker  in my_document:
                    my_document[current_speaker]=[]
                my_document[current_speaker].append(line)


print len(my_document)

for speaker in my_document:
    print speaker, len(my_document[speaker])
    #print my_document[speaker]

