#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:44:18 2023

@author: tatianalenskaia
"""

path = "/Users/tatianalenskaia/HMM/Rset/HMMs Edited/"

#fInName = "Rset_TIGRFAM_25.txt"
#fInName = "TIGRFAM_release15_list.txt"
fInName = "Rset_Custom_275.txt"



fOutName = "Rset_Custom_275_script_sequence_cds.txt"

fOut = open(path+fOutName,"w")

i = 0
c = 0


s1 = "hmmsearch --domtblout "
s2 = ".out "
s3 = ".HMM "


#s4 = "phrogs_update.faa"
s4 = "sequence_cds.faa"

fIn = open(path+fInName, "r")
for line in fIn:
    line = line.strip()
    i = i+1
    print(i,line)
    
    s = s1+s4.split(".")[0]+"_"+line+s2+line+s3+s4
    
    fOut.write(s+"\n")
    
    '''
    fIn1 = open(path+line+".HMM")
    #fIn1 = open(path+line)
    for ln in fIn1:
        if ln != "\n":
            fOut.write(ln)
        else:
            c += 1
    fIn1.close()
    '''
    
fIn.close()
fOut.close()
print(c)