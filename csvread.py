
 #%%
import re
import numpy as np
from copy import deepcopy
import glob
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from bs4 import BeautifulSoup as bs
from nltk.tokenize import word_tokenize
from many_stop_words import get_stop_words
from collections import Counter

foldernamelist = []
foldernamelistNew = []
foldernamelistTitle = []
ListOfStagsPerFolder = []

Stemmer = PorterStemmer()

def TagExtractionFuction(String):
    string = String
    for alltagsExtr in soup.find_all(string):
            titletagslines = []
            tt = "".join(str(alltagsExtr))
            soup2 = bs(tt, "html.parser")
            Ttag = "".join(str(soup2.text))
            Ttags = re.sub(r'[\'\n]','', Ttag)
            
            TtagsWT = Ttags.split()   #tokenizing
            for Twords in TtagsWT:  
                #Twords = Twords.strip()#stopwords removing
                if Twords not in totalstopwords: #stopwords removing
                    
                    Twordss = re.sub(r'\\n', '',Twords)
                    Twordss = Twordss.replace('\s', "")
                    words2 = Stemmer.stem(Twordss)
                    titletagslines.append(words2)
            titletagslines1.append(titletagslines)
mystopwords = ['&','#','*','A','--','$','\\','_',"'n","'",'\\n',"', '","n't","'s","'\\n",' ',',','.','"','""',"''",'``',':','?','I','%','+','!','(',')','-',';','The']
stpw = list(get_stop_words('en'))
totalstopwords = mystopwords + stpw
for i in glob.glob("C:/Users/aa/.spyder/dataset/docs.with.sentence.breaks/*"):
file = np.array("")
print(file)