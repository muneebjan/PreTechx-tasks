# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import documentExtraction as f1
import re
import nltk
import glob
from many_stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup as bs
Sumfoldernamelist = []
Sumfilenamelist = []
snow = nltk.stem.SnowballStemmer('english')
mystopwords = ["'","\\n","', '","n't","'s","'",' ',',','.','"','""',"''",'``',':','?','I','%','+','!','(',')','-',';','The']
stpw = list(get_stop_words('en'))
totalstopwords = mystopwords + stpw    
for i in glob.glob("C:/Users/aa/Downloads/duc2002extracts/*"):    
    Fullsumlist = []
    for j in glob.glob(i+"/400e"):
        list1 = []
        fileread = open(j, "r")
        listoffiles = fileread.readlines()
        Sumfilenamelist.append(listoffiles)
        for x in Sumfilenamelist:
            text = "".join(str(x))
        soup = bs(text, "html.parser")
        for z in soup.find_all('s'):
            sumanotherlist = []
            st = "".join(str(z))
            soup2 = bs(st, "html.parser")
            Stag = "".join(str(soup2.text))
            Stags = re.sub("[']", '', Stag)
            StagsWT = word_tokenize(Stags)   #tokenizing
            for words in StagsWT:             #stopwords removing
                if words not in totalstopwords: #stopwords removing
                    words2 = snow.stem(words)        
                    sumanotherlist.append(words)
                    #stopwords removing
            list1.append(sumanotherlist)
        Fullsumlist.append(list1)
    Sumfoldernamelist.append(Fullsumlist)
"""
Comparing the lines within the files.
"""
allsent = []
NewSumlist = []
NewSumlist1 = []
matchedsummlist = []
uniquesummlistfile = []
totalsentences = []
count = 0
count1 = 0
count2 = 0
for cc in Sumfoldernamelist[0::2]:
        NewSumlist.append(cc)
for cc in Sumfoldernamelist[1::2]:
        NewSumlist1.append(cc)
for mm in NewSumlist:
    nonmatchedsummlist = []
    for stagsumm in NewSumlist[count][count1]:
        for stagsumm1 in NewSumlist1[count][count1]:
            if stagsumm == stagsumm1:           
                matchedsummlist.append(stagsumm)                
            if not stagsumm == stagsumm1:            
                if not stagsumm in nonmatchedsummlist:
                    nonmatchedsummlist.append(stagsumm)
                if not stagsumm1 in nonmatchedsummlist:
                    nonmatchedsummlist.append(stagsumm1)               #allsent.append(nonmatchedsummlist)

    uniquesummlistfile.append(nonmatchedsummlist)
    count += 1
    #end for
#end for


for outer in uniquesummlistfile:
    for inner in outer:
        allsent.append(inner)
        
count2 = len(allsent)

count3 = 0
count4 = 0
count5 = 0
summarysentences = []
nonsummarysentences = []
cv = 0



for outerlist in uniquesummlistfile: #0-58indexes
    for innerlist in uniquesummlistfile[count3]:
        
        for datalist in f1.foldernamelist[count3]:
            for innerdatalist in datalist:
                if innerlist == innerdatalist:
                    #if innerlist not in summarysentences:
                    summarysentences.append(innerlist)
                    #print("!!!!!!! WARNING !!!!!!! \n MATCHED",innerlist,innerdatalist)
                if not innerlist == innerdatalist:
                    if innerdatalist not in nonsummarysentences:
                        nonsummarysentences.append(innerdatalist)
                    #print("------- NOT MATCHED --------",innerlist,innerdatalist)
                cv+=1
                #print(cv)
                
            break       #1 sentences compares with all 6 files
        break       #all lines of Index 0 will be compared
    #count3+=1
    break        
    








