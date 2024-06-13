#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:36:05 2023

@author: tatianalenskaia
"""


# TIGRFAM collection
path1 = "/Users/tatianalenskaia/HMM/TIGRFAMs_15.0_HMM/"





# list of specific HMMs
path2 = "/Users/tatianalenskaia/HMM/From Alan/updated_yes_maybe_682/"
fInName = "TIGRFAM_19.txt"

# A subset of HMMs specified in the list
fOutName = fInName.split(".")[0]+".HMM"





'''
fInName = "Rset_TIGRFAM_25.txt"
fInName = "TIGRFAM_release15_list.txt"

fOutName = "Rset_TIGRFAM_25.hmm"
fOutName = "TIGRFAM_release15.hmm"
'''

fOut = open(path2+fOutName,"w")

i = 0

fIn = open(path2+fInName, "r")
for line in fIn:
    line = line.strip()
    i = i+1
    print(i,line)
    fIn1 = open(path1+line+".HMM")
    #fIn1 = open(path1+line)
    for ln in fIn1:
        fOut.write(ln)
    fIn1.close()
fIn.close()
fOut.close()