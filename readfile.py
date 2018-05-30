
from copy import deepcopy
import glob
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from bs4 import BeautifulSoup as bs
fro import re
m n collections import Counter
import numpy as np

foldernamelist = []
foldernamelistNew = []
foldernamelistTitle = []
ListOfSltk.tokenize import word_tokenize
from nltk.corpus import stopwords
fromtagsPerFolder = []

Stemmer = PorterStemmer()
mystopwords1 = ['/','',' ','&','#','*','A','--','$','\\','_',"'n","'",'\\n',"', '","n't","'s","'\\n",' ',',','.','"','""',"''",'``',':','?','I','%','+','!','(',')','-',';','The']
stpw1 = list(stopwords.words('english'))

totalstopwords1 = mystopwords1 + stpw1
[]
mychecklist1 = []
def TagExtractionFu
mychecklist = ction(String):
    string = String
    for alltagsExtr in soup.find_all(string):
            titletagslines = []
            tt = "".join(str(alltagsExtr))
            soup2 = bs(tt, "html.parser")
            Ttag = "".join(str(soup2.text))
            mychecklist.append(Ttag)
            Ttags = re.sub(r"[\n,']",'', Ttag)
            mychecklist1.append(Ttags)
            TtagsWT = Ttags.split()   #tokenizing
            for Twords in TtagsWT:  
                #Twords = Twords.strip()#stopwords removing
                if Twords not in totalstopwords1: #stopwords removing
                    #print(Twords)
                    Twordss = Stemmer.stem(Twords)
                    Twordss1 = re.sub(r"[\n;:]",'',Twordss)
                    #Twordss1 = re.sub(r"[\\n]",'',Twordss)
                    words2 = Twordss1.replace('\\n', "")
                    #words2 = Stemmer.stem(Twordss1)
                    
                    titletagslines.append(words2)
            titletagslines1.append(titletagslines)





mystopwords = ['&','#','*','A','--','$','\\','_',"'n","'",'\\n',"', '","n't","'s","'\\n",' ',',','.','"','""',"''",'``',':','?','I','%','+','!','(',')','-',';','The']
stpw = list(stopwords.words('english'))

totalstopwords = mystopwords + stpw

for i in glob.glob("C:/Users/aa/.spyder/dataset/docs.with.sentence.breaks/*"):
    filenamelist = []
    filenamelist1 = []
    filenamelist2 = []
    filenamelisttitle = []
    ListOfStagsPerFile = []
    for j in glob.glob(i+"/*"):
        ListOfStagsIn_a_File = []
        list1 = []
        list2 = []
        titletagslines1 = []
        
        fileread = open(j, "r")
        listoffiles = fileread.readlines()
        #print(len(listoffiles))
        filenamelist.append(listoffiles) 
        
        for x in filenamelist:
            text = "".join(str(x))
        soup = bs(text, "html.parser")

        
        
        TagExtractionFuction('headline')
    
        TagExtractionFuction('head')
    
        TagExtractionFuction('hl')
    
        TagExtractionFuction('h3')
        

        for y in soup.find_all('text'):
            t = "".join(str(y))
        s = bs(t, "html.parser")
        
        for z in s.find_all('s'):
            anotherlist = []
            anotherlist1 = []
            st = "".join(str(z))
            soup2 = bs(st, "html.parser")
            Stag = "".join(str(soup2.text))
            if Stag == ' . . .':
                del Stag
            elif Stag == ' I':
              del Stag
           
            else:
                Stags = re.sub(r'[\\.]' , '', Stag)
                ListOfStagsIn_a_File.append(Stags)
                StagsWT = word_tokenize(Stags)  #tokenizing
                for words in StagsWT:               #stopwords removing
                    if words not in totalstopwords: #stopwords removing
                        words2 = Stemmer.stem(words)
                        words3 = re.sub(r"[']" , '', words2)
                        anotherlist.append(words3)   #stopwords removing
                
                if not len(anotherlist) == 0:
                    list1.append(anotherlist)
                    
                for words1 in StagsWT:               #stopwords removing
                    if words1 not in totalstopwords: #stopwords removing
                        words1 = re.sub(r"[,``''-]" , '', words1)
                        anotherlist1.append(words1)   #stopwords removing
                
                if not len(anotherlist1) == 0:
                    list2.append(anotherlist1)
            #list1.append(Stags)
            #break                    #innerfurther break
        #break                        #inner loop break
    #break                            #outer loop break
    
        ListOfStagsPerFile.append(ListOfStagsIn_a_File)
        filenamelist1.append(list1)
        filenamelist2.append(list2)
        filenamelisttitle.append(titletagslines1)
        if len(titletagslines1) == 0:
            titletagslines1.insert(filenamelisttitle.index(titletagslines1),"NAN")
        
    ListOfStagsPerFolder.append(ListOfStagsPerFile)    
    foldernamelist.append(filenamelist1)
    foldernamelistNew.append(filenamelist2)
    foldernamelistTitle.append(filenamelisttitle)