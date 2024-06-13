#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:23:29 2023

@author: tatianalenskaia
"""


import core_methods as cm

path = "/Users/tatianalenskaia/_ShC_phages/230601_Clustering/HMM_res/"


fInName = "312phages_phages_HMMres_PAT.txt"
res = cm.GetDictFromFile(path+fInName, "\t", 1, 0)

d = res[1]
print(len(d))


fInName = "312phages_cds.faa"

label = "312phages"
ftype = "faa"


fIn = open(path+fInName,"r")
lines = fIn.readlines()
fIn.close()
n = len(lines)
print(n)


fOutName = fInName.rsplit(".")[0]+"_annot_hmmname."+fInName.rsplit(".")[1]
fOut = open(path+fOutName, "w")


for i in range(0,n,2):
    #print(line)
    #print(i, lines[i])
    
    if ftype == "faa":
        t_line = lines[i][1:].strip().split("|")
        #print(t_line)
        i_id = t_line[0]+"|"+t_line[1]
        #print(i_id)
        cat = "!"
        if i_id in d:
            cat = d[i_id][1]
            hmm = d[i_id][3]
            print(cat, hmm)
            if cat == "":
                cat = "-"

        fOut.write(">CAT["+cat+"]|"+lines[i][1:])
        fOut.write(lines[i+1])
    break
fOut.close()
    

