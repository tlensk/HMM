#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:06:59 2023

@author: tatianalenskaia
"""


path = "/Users/tatianalenskaia/HMM/Rset/hmm2hhm/"


fInName = "Rset_Pfam_462.hmm"


i = 0
tt = []


d = {}

fIn = open(path+fInName, "r")
for line in fIn:

    i = i+1
    
    tt.append(line)

    if line[0:2] == "//":
        
        if "ACC" in tt[2]:
            nm = tt[2].split()[1]
            fOut = open(path+nm+".HMM","w")
            
            for it in tt[0:(-1)]:
                #print(it)
                fOut.write(it)
            fOut.write(tt[-1].strip())
            fOut.close()

        tt = []
        break

        
    '''    
    if i > 5:
        break
    '''
#print(tt[2])


