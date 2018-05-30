# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import re
from copy import deepcopy
import glob
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
from bs4 import BeautifulSoup as bs
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import numpy as np

import SentSimilarity as ss



foldernamelist = []
foldernamelistNew = []
foldernamelistTitle = []
ListOfStagsPerFolder = []

Stemmer = PorterStemmer()
mystopwords1 = ['/','',' ','&','#','*','A','--','$','\\','_',"'n","'",'\\n',"', '","n't","'s","'\\n",' ',',','.','"','""',"''",'``',':','?','I','%','+','!','(',')','-',';','The']
stpw1 = list(stopwords.words('english'))

totalstopwords1 = mystopwords1 + stpw1

mychecklist = []
mychecklist1 = []
def TagExtractionFuction(String):
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

#%%
'''
////////////// First Feature Extraction \\\\\\\\\\\\\\\
F1 = number of title words in sentence / number of words in document title
'''
#%%
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
                Feature = [float("{0:.3f}".format(round(Feature,3)))]
                titleWlist1.append(Feature)
                #break
            titleWlist2.append(titleWlist1)
            print('End of File: ',len(titleWlist2))
            perfilecounter+=1
            #break
            
        #indexx+=1            
        #if len(mm) == 0:
            #print('------------------------',indexx,'----------------------------')
            #mm.insert(indexx,"NAN")
            
        #break
    # ======== End of 1st Folder ==========   
    count+=1
    FeaturesList.append(titleWlist2)
    Feature1List.append(deepcopy(titleWlist2))
    
    print("=============",count,"Folder Ends==============")
    #break
# ======== End of ALL Folder ==========
#%%
"""
////////// Extracting Feature 2 \\\\\\\\\\\
f2 = Sentences Similarity

""" 
#%%

Feature2List = []
ef = 0
coun = 0
sumvalues = 0
for out in ListOfStagsPerFolder:
    newfeatlistf2 = []
    ccc = 0
    for inn in out:
        featlist = []
        f2featlist = []
        for inner in inn:
            
            for perfilesent in ListOfStagsPerFolder[ef][ccc]:
                if inner != perfilesent:
                    totalvalues = ss.semanticSimilarity(inner, perfilesent)
                    sumvalues = sumvalues + totalvalues  
            featlist.append(sumvalues)
            sumvalues = 0
            
            #break
        ccc+=1
        print('End of File',ccc)
        newfeatlistf2.append(f2featlist)
        break
    ef+=1
    print('=============End of Folder==============',ef)
    Feature2List.append(newfeatlistf2)
    break
print("============  End of Feature-3  ============")





#%%
'''
////////// Extracting Feature 3 \\\\\\\\\\\
f3 = length of document − sentence position+1/length of document

'''
#%%  
Feature3List = []
ef = 0
for out in foldernamelist:
    newfeatlist = []
    ccc = 0
    for inn in out:
        featlist = []
        for inner in inn:
            feature = (len(inn) - ((inn.index(inner))+1)) / float(len(inn))
            feature = [float("{0:.3f}".format(round(feature,3)))]
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
print("============  End of Feature-3  ============")


#%%
"""
////////// Extracting Feature 4 \\\\\\\\\\\
f4 = number of numerical data in the sentence/length of sentence

""" 
#%%

Feature4List = []
ef4 = 0
for f4out in foldernamelistNew:
    f4featlist1 = []
    c4 = 0
    for f4inn in f4out:
        f4featlist = []
        for f4inner in f4inn:
            s44 = ''.join(w4 for w4 in f4inner)
            numdata = re.findall('\d+',s44)
            feature4 = len(numdata) / float(len(f4inner))
            feature4 = [float("{0:.3f}".format(round(feature4,3)))]
            f4featlist.append(feature4)
            #break

        c4+=1
        print('End of File',c4)
        f4featlist1.append(f4featlist)
        #break
    ef4+=1
    print('=============End of Folder==============',ef4)
    Feature4List.append(f4featlist1)
    #break

print("============  End of Feature-4  ============")

#%%

"""
////////////////////////////////////////////////////////
////////// FUNCTION TO POPULATE FEATURESLIST \\\\\\\\\\\
////////////////////////////////////////////////////////
""" 
#%%

def populateFeaturesList(givenlist):

    f5c1 = 0  
    f5c2 = 0
    f5c3 = 0
    
    for fold in givenlist:
        for fil in fold:
            for filinner in fil:
                #Feature6List[f5c1][f5c2][f5c3].append(filinner)
                #print((f5c1,f5c2,f5c3),filinner)
                #print((f5c1,f5c2,f5c3),Feature6List[f5c1][f5c2][f5c3])
                FeaturesList[f5c1][f5c2][f5c3].extend(filinner)
                f5c3+=1
                #break
            f5c3 = 0
            f5c2+=1
            #break
        f5c3 = 0
        f5c2 = 0
        f5c1+=1
        #break
        


#%%
"""
////////// Extracting Feature 5 \\\\\\\\\\\
f5 = number of temporal information in the sentence/length of sentence

"""  
#%%


Feature5List = []
timepattern = r"(?:\d{1,2}\s?[AaPp][Mm]) | (?:\d{1,2}\s?:\d{2}\s?[AaPp][Mm])" 
datepattern = r"((?:1\d{3}|20\d{2})|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{1,2} | (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s?\d{1,2},?\s?1\d{3}|20\d{2})" 
ef5 = 0
f5c = 0
f5c1 = 0
f5c2 = 0
for f5out in ListOfStagsPerFolder:
    f5featlist1 = []
    c5 = 0
    for f5inn in f5out:
        f5featlist = []
        for f5inner in f5inn:
            teststr = "its Feb 3, 1994 and 1995 and Mar 3 here in morning"
            matcher = re.findall(timepattern, f5inner)
            matcher1 = re.findall(datepattern, f5inner)
            matcher2 = matcher+matcher1
            #print(len(matcher2))
            #print(foldernamelistNew[f5c][f5c1][f5c2])
            #print(ListOfStagsPerFolder.index(f5out),f5out.index(f5inn),f5inn.index(f5inner))
            #print(len(foldernamelistNew[ListOfStagsPerFolder.index(f5out)][f5out.index(f5inn)][f5inn.index(f5inner)]))
            feature5 = len(matcher2) / float(len(foldernamelistNew[ListOfStagsPerFolder.index(f5out)][f5out.index(f5inn)][f5inn.index(f5inner)]))
            feature5 = [float("{0:.3f}".format(round(feature5,3)))]
            f5c2+=1
            f5featlist.append(feature5)
            #break
        f5c2= 0
        f5c1+=1
        c5+=1
        print('End of File',c5)
        f5featlist1.append(f5featlist)
        #break
    f5c1 = 0
    f5c2= 0
    f5c+=1    
    ef5+=1
    print('=============End of Folder==============',ef5)
    Feature5List.append(f5featlist1)
    #break

print("============  End of Feature-5  ============")

#%%

"""
////////// Extracting Feature 6 \\\\\\\\\\\
f6 = number of words occuring in the sentence/number of words occuring in the longest sentence

"""  
#%%    

Feature6List = []
ef6 = 0
for f6out in foldernamelist:
    f6featlist1 = []
    c6 = 0
    for f6inn in f6out:
        f6featlist = []
        for f6inner in f6inn:
            featuref6 = (len(f6inner)) / float(len(max(f6inn,key=len)))
            featuref6 = [float("{0:.3f}".format(round(featuref6,3)))]
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

print("============  End of Feature-6  ============")

#%%
   
"""
////////// Extracting Feature 7 \\\\\\\\\\\
f7 = number of proper nouns in the sentence/length of sentence

"""  
#%%

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
            feature7 = [float("{0:.3f}".format(round(feature7,3)))]
            f7featlist.append(feature7)
            #break
        #c7+=1
        #print('End of File',c7)
        f7featlist1.append(f7featlist)
        #break
    #ef7+=1
    #print('=============End of Folder==============',ef7)
    Feature7List.append(f7featlist1)
    #break

print("============  End of Feature-7  ============")

#%%

"""
////////// Extracting Feature 8 \\\\\\\\\\\
f8 = number of nouns&Verbs in a sentence/length of sentence

"""  

#%%

Feature8List = []
ef8 = 0
for f8out in foldernamelistNew:
    f8featlist1 = []
    c8 = 0
    for f8inn in f8out:
        f8featlist = []
        for f8inner in f8inn:
            tagged_sent8 = pos_tag(f8inner)
            #print(tagged_sent8)
            propernouns8 = [word8 for word8,pos8 in tagged_sent8 if (pos8 == 'NNS' or pos8 == 'NN' or
                                                                     pos8 == 'VBD' or pos8 == 'VBN' or
                                                                     pos8 == 'VBP')]
            #print('Length of PPN: ',len(propernouns))
            #print('Length of Sentence: ',len(f7inner))
            feature8 = len(propernouns8) / float(len(f8inner))
            feature8 = [float("{0:.3f}".format(round(feature8,3)))]
            f8featlist.append(feature8)

        #c8+=1
        #print('End of File',c7)
        f8featlist1.append(f8featlist)
        #break
    #ef8+=1
    #print('=============End of Folder==============',ef8)
    Feature8List.append(f8featlist1)
    #break
print("============  End of Feature-8  ============")   

#%%

"""
////////// Converting all Data to single string PER FILE \\\\\\\\\\\\\\

"""

#%%

AllDataString = []
for alldataouter in foldernamelist:
    AllDataStringPerFolder = []
    for alldatainn in alldataouter:
        AllDataStringPerFile = []
        for alldatainner in alldatainn:
            sti = " ".join(w for w in alldatainner)
            remextra = re.sub(r"[-`'_]" , '', sti)
            wordstokenizer = word_tokenize(remextra)
            AllDataStringPerFile.extend(wordstokenizer)
            #break
        AllDataStringPerFolder.append(AllDataStringPerFile)
        #break
    AllDataString.append(AllDataStringPerFolder)
    #break

#%%


"""
////////// Extracting Feature 9 \\\\\\\\\\\
f9 = number of frequent terms in the sentence/max(number of frequent terms)

"""  

#%%

c9count1 = 0
c9count = 0  
Feature9List = []
for f9out in foldernamelist:
    f9featlist1 = []
    for f9inn in f9out:
        f9featlist = []
        for f9inner in f9inn:
            AChecklist = []
            freqPerFile = Counter(AllDataString[foldernamelist.index(f9out)][f9out.index(f9inn)])
            top10perfile = freqPerFile.most_common(10)
            for wordsintop10out in top10perfile:
                for f9innerext in f9inner:                    
                    if wordsintop10out[0] == f9innerext:
                        #print("|||||-MATCHED-|||||",wordsintop10out[0],f9innerext)
                        if f9innerext not in AChecklist:
                                AChecklist.append(wordsintop10out[0])
                    #else:
                        #print("====NOT-MATCHED====",wordsintop10out[0],f9innerext)
                    #break
                #break            
            #print(len(AChecklist))
            #print(len(top10perfile))
            feature9 = len(AChecklist) / float(len(wordsintop10out))
            feature9 = [float("{0:.3f}".format(round(feature9,3)))]
            f9featlist.append(feature9)
            #break
        f9featlist1.append(f9featlist)
        #break
    Feature9List.append(f9featlist1)
    #break
#%%
"""
////////////////////////////////////////////////////////
\\\\\\\\\\ CALLING FUNCTION TO POPULATE \\\\\\\\\\\
////////////////////////////////////////////////////////
""" 
#%%

populateFeaturesList(Feature3List)
populateFeaturesList(Feature4List)
populateFeaturesList(Feature5List)
populateFeaturesList(Feature6List)
populateFeaturesList(Feature7List)
populateFeaturesList(Feature8List)
populateFeaturesList(Feature9List)



#%%
"""
////////////////////////////////////////////////////////
\\\\\\\\\\ ENDING OF THE FUNCTION POPULATE \\\\\\\\\\\
////////////////////////////////////////////////////////
""" 

#%%

#=======================================================
#======== Single List Containing All Features ==========
#=======================================================

SingleListContainingFeatures = []

for outersl in FeaturesList:
    for innsl in outersl:
        for innersl in innsl:
            SingleListContainingFeatures.append(innersl)

#=========================END===========================
#======== Single List Containing All Features ==========
#=========================END===========================
            
            
#%%
            
            
#=======================================================
#======= POPULATING NUMPY ARRAY WITH FEATURES ==========
#=======================================================

NumpyFeatures = np.vstack([SingleListContainingFeatures])
print(np.shape(NumpyFeatures))

#=========================END===========================
#======= POPULATING NUMPY ARRAY WITH FEATURES ==========
#=========================END===========================



#%%





















