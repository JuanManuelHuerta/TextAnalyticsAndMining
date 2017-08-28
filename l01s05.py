import sys
from bs4 import BeautifulSoup
import re
import operator


def cosine_distance(text1,text2):
    text_vocab1 = set(w.lower() for w in text1 if w.isalpha())
    text_vocab2 = set(w.lower() for w in text2 if w.isalpha())
    distance = float(len(text_vocab1.intersection(text_vocab2)))/(len(text_vocab1)*len(text_vocab2))
    return  distance




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
                my_document[current_speaker]+=line.split()


print len(my_document)

for speaker_1 in my_document:
    for speaker_2 in my_document:
        if speaker_1>speaker_2:
            print speaker_1, speaker_2, cosine_distance(my_document[speaker_1],my_document[speaker_2])
    #print my_document[speaker]

