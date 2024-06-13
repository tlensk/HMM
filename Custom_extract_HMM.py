#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:44:18 2023

@author: tatianalenskaia
"""

#path = "/Users/tatianalenskaia/HMM/Rset/HMMs Edited/"
path = "/Users/tatianalenskaia/HMM/All_HMMs/"

#fInName = "Rset_TIGRFAM_25.txt"
#fInName = "TIGRFAM_release15_list.txt"
#fInName = "Rset_Custom_275.txt"
#fInName = "Custom_268.txt"


fInName = "Custom_LT.txt"




#fOutName = "Rset_TIGRFAM_25.hmm"
#fOutName = "TIGRFAM_release15.hmm"

'''
fOutName1 = "Rset_Custom_67_b.hmm"
fOutName2 = "Rset_Custom_208_f.hmm"
'''



fOutName1 = "Custom_LT_b.hmm"
fOutName2 = "Custom_LT_f.hmm"



fOut1 = open(path+fOutName1,"w")
fOut2 = open(path+fOutName2,"w")



i = 0
ct = 0

d_f = {}

fIn = open(path+fInName, "r")
for line in fIn:
    line = line.strip()
    i = i+1

    fIn1 = open(path+line+".HMM")
    #fIn1 = open(path+line)
    lines1 = fIn1.readlines()
    header = lines1[0]
    t_header = header.split()
    ver = t_header[0]
    print(i,ver, line)
    
    if ver not in d_f:
        d_f[ver] = []
    d_f[ver].append(line)
    
    #print(t_header)
    if ver == "HMMER3/b":
        for ln in lines1:
            if ln != "\n":
                fOut1.write(ln)

    if ver == "HMMER3/f":
        for ln in lines1:
            if ln != "\n":
                fOut2.write(ln)



    fIn1.close()
fIn.close()

fOut1.close()
fOut2.close()




print(ct)

for it in d_f:
    print(it, len(d_f[it]))








"""
fOutName = "Rset_Custom_275_script.txt"

fOut = open(path+fOutName,"w")

i = 0
c = 0


s1 = "hmmsearch --domtblout "
s2 = ".out "
s3 = ".HMM phrogs_update.faa"

fIn = open(path+fInName, "r")
for line in fIn:
    line = line.strip()
    i = i+1
    print(i,line)
    
    s = s1+line+s2+line+s3
    
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
"""