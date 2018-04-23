# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
from copy import deepcopy
import glob
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from bs4 import BeautifulSoup as bs
from nltk.tokenize import word_tokenize
from many_stop_words import get_stop_words
foldernamelist = []
foldernamelistNew = []
foldernamelistTitle = []

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





mystopwords = ['$','\\','_',"'n","'",'\\n',"', '","n't","'s","'\\n",' ',',','.','"','""',"''",'``',':','?','I','%','+','!','(',')','-',';','The']
stpw = list(get_stop_words('en'))

totalstopwords = mystopwords + stpw

for i in glob.glob("C:/Users/aa/.spyder/dataset/docs.with.sentence.breaks/*"):
    filenamelist = []
    filenamelist1 = []
    filenamelist2 = []
    filenamelisttitle = []
    for j in glob.glob(i+"/*"):
        
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
            Stags = re.sub(r'[\\.]' , '', Stag)
            StagsWT = word_tokenize(Stags)  #tokenizing
            for words in StagsWT:               #stopwords removing
                if words not in totalstopwords: #stopwords removing
                    words2 = Stemmer.stem(words)
                    anotherlist.append(words2)   #stopwords removing
            
            if not len(anotherlist) == 0:
                list1.append(anotherlist)
                
            for words1 in StagsWT:               #stopwords removing
                if words1 not in totalstopwords: #stopwords removing
                    words1 = re.sub(r"[,``'']" , '', words1)
                    anotherlist1.append(words1)   #stopwords removing
            
            if not len(anotherlist1) == 0:
                list2.append(anotherlist1)
            #list1.append(Stags)
            #break
        #break
    #break

        filenamelist1.append(list1)
        filenamelist2.append(list2)
        filenamelisttitle.append(titletagslines1)
    foldernamelist.append(filenamelist1)
    foldernamelistNew.append(filenamelist2)
    foldernamelistTitle.append(filenamelisttitle)


'''
////////////// First Feature Extraction \\\\\\\\\\\\\\\
'''
FeaturesList = []
Feature1List = []
count = 0
for jj in foldernamelistTitle:
    indexx = 0
    count1 = 0
    perfilecounter = 0
    titleWlist2 = []
        
    for mm in foldernamelistTitle[count]: #Calculates Per Folder according to the Index.
        titleWlist1 = []
        count2 = 0
        if not len(mm) == 0:
            for nn in foldernamelist[count][perfilecounter]: #per file 
                AtitleWlist =[]
                totalTitleWords = 0
                Feature = 0
                sentcount = 0
                for wordinTitleSentence in mm[count1]:
                    for wordinSentence in nn:
                        if wordinTitleSentence == wordinSentence:
                            #print("Matched",wordinTitleSentence,wordinSentence)
                            if wordinTitleSentence not in AtitleWlist:
                                AtitleWlist.append(wordinTitleSentence)
                        #if not wordinTitleSentence == wordinSentence:
                            #print("Not Matched",wordinTitleSentence,wordinSentence)
                    sentcount+=1
                    #print("End of Sentence: ",sentcount)
                    totalTitleWords+=1
                    #break
                count2+=1
                #print("End of Sentence Title: ",count2)
                Feature = len(AtitleWlist)/float(totalTitleWords)
                Feature = [Feature]
                titleWlist1.append(Feature)
                #break
            titleWlist2.append(titleWlist1)
            print('End of File: ',len(titleWlist2))
            perfilecounter+=1
            #break
        indexx+=1            
        if len(mm) == 0:
            mm.insert(indexx,"NAN")
        #break
    # ======== End of 1st Folder ==========   
    count+=1
    FeaturesList.append(titleWlist2)
    Feature1List.append(deepcopy(titleWlist2))
    
    print("=============",count,"Folder Ends==============")
    #break
# ======== End of ALL Folder ==========
    

Feature3List = []
ef = 0
for out in foldernamelist:
    newfeatlist = []
    ccc = 0
    for inn in out:
        featlist = []
        for inner in inn:
            feature = (len(inn) - ((inn.index(inner))+1)) / float(len(inn))
            featlist.append(feature)
            #Feature1List[foldernamelist.index(out)][out.index(inn)][inn.index(inner)].append(feature)
            #break
        ccc+=1
        print('End of File',ccc)
        newfeatlist.append(featlist)
        #break
    ef+=1
    print('=============End of Folder==============',ef)
    Feature3List.append(newfeatlist)
    #break
"""
////////// COMBINING FEATURES TO SINGLE LIST \\\\\\\\\\\

"""    

for fold in Feature3List:
    for fil in fold:
        for feat in fil:
            #Feature1List[Feature2List.index(fold)][fold.index(fil)][fil.index(feat)].append(feat)
            break
        break
    break

"""
////////// Extracting Feature 6 \\\\\\\\\\\
f6 = number of words occuring in the sentence/number of words occuring in the longest sentence

"""  
    

Feature6List = []
ef6 = 0
for f6out in foldernamelist:
    f6featlist1 = []
    c6 = 0
    for f6inn in f6out:
        f6featlist = []
        for f6inner in f6inn:
            featuref6 = (len(f6inner)) / float(len(max(f6inn,key=len)))
            f6featlist.append(featuref6)
            #break
        c6+=1
        print('End of File',c6)
        f6featlist1.append(f6featlist)
        #break
    ef6+=1
    print('=============End of Folder==============',ef6)
    Feature6List.append(f6featlist1)
    #break
    
"""
////////// Extracting Feature 7 \\\\\\\\\\\
f7 = number of proper nouns in the sentence/length of sentence

"""  


Feature7List = []
ef7 = 0
for f7out in foldernamelistNew:
    f7featlist1 = []
    c7 = 0
    for f7inn in f7out:
        f7featlist = []
        for f7inner in f7inn:
            tagged_sent = pos_tag(f7inner)
            propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
            #print('Length of PPN: ',len(propernouns))
            #print('Length of Sentence: ',len(f7inner))
            feature7 = len(propernouns) / float(len(f7inner))
            #print(feature7)
            f7featlist.append(feature7)
            #break
        c7+=1
        #print('End of File',c7)
        f7featlist1.append(f7featlist)
        #break
    ef7+=1
    print('=============End of Folder==============',ef7)
    Feature7List.append(f7featlist1)
    #break

    