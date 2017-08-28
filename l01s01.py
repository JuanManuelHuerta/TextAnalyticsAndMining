import sys
from bs4 import BeautifulSoup
import re

fp=open("obama_debate.html","rt")
html_doc=fp.read()
od = BeautifulSoup(html_doc, 'html.parser')
#print(dps.prettify())
current_speaker=""
# Beautiful soup
i=0
my_document={}
current_blank=False

for turn in od.p:
    turn_string=str(turn.string)
    i+=1
    my_split=turn_string.split()
    if len(my_split)>0:
        if re.match(r"^[A-Z]+\:$",my_split[0]):
            candidate_speaker=my_split[0].replace(":","")
        else:
            candidate_speaker=""
    else:
        candidate_speaker=""
#    print "speaker", candidate_speaker
    if candidate_speaker!="":
        current_speaker=candidate_speaker
        modified_line=' '.join(my_split[1:])
    else:
        modified_line=turn_string
    if current_speaker!="":
        if not current_speaker  in my_document:
            my_document[current_speaker]=[]
        my_document[current_speaker].append(modified_line)
for speaker in my_document:
    fp=open(speaker+".txt","wt")
    fp.write(" ".join(my_document[speaker]))
    fp.close()



