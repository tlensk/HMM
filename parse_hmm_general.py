#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:28:34 2023

@author: tatianalenskaia
"""

import hmmout_parse_lib as hpl




path = "/Users/tatianalenskaia/_ShC_phages/HO-PG-IN/PAT_HO/"
fInName =  "PAT_HO_all.out"







d_pid = []

fIn = open(path+fInName, "r")

lines = []
for line in fIn:
    if line[0] != "#":
        lines.append(line.strip())
    

fIn.close()

print(len(lines))


ReadInHMMout(path_out, t_list, d_pid, ftype):
'''








t_list = ["Aset_Custom_b.out",
          "Aset_Custom_f.out",
          "Pfam-A.out",
          "TIGRFAM_release15.out"]


#t_list = ["Aset_Custom_b.out"]

t_list = ["PAT_HO_all.out"]



#---------- Read-in hmm.out files

hmm_res = hpl.ReadInHMMout(path_out, t_list, d_pid,ftype)

d_hmm_res = hmm_res[0]
d_hmm_prs = hmm_res[1]





#print(len(t_hmm))

fOutName = label+"_phages_HMMres_PAT.txt"
fOut = open(path_out+fOutName, "w")
#print("Genome_id|Protein_id",	"Location", "Initial_annotation","Number_of_HMM_hits","Category", "Details_about_HMM_hits [category,function, hmm_id, hmm_accession, hmm_name, e-value]", sep = "\t", file = fOut)

print("Genome_id|Protein_id",	"Number_of_HMM_hits","Category", "Details_about_HMM_hits [category,function, hmm_id, hmm_accession, hmm_name, e-value]", sep = "\t", file = fOut)
fOut.close()


#fOutName1 = label+"_phages_patterns.txt"
#fOut1 = open(path_out+fOutName1, "w")




d_i_id = {}
t_i_id = []
thr = 100
cc = 0

st = label

for i_id in d_pid:
    
    print(i_id)
    
    
    ttt = []
    c = 0
    #st = i_id
    
    i_id_gr = "hypothetical protein"
    cat = ""
    t_i_id.append(i_id)
    
    if i_id in d_hmm_prs:
        tt1 = d_hmm_prs[i_id]
        tt = sorted(tt1, key = lambda tt1: tt1[-4])
    
        fl_pat = 0
        for item in tt:
            if (item[0] in t_hmm) and (item[-4]< thr):
                hmm = item[0]
                lb = ""
                fn = ""
                if hmm in d_hmm_aset:
                    lb = d_hmm_aset[hmm][0]
                    fn = d_cat_fun[lb]
                    if fl_pat == 0:
                        i_id_gr = fn
                        cat = lb
                        fl_pat = 1
                ttt.append([lb]+[fn]+item[0:4])
                c += 1
        
    if i_id not in d_i_id:
        d_i_id[i_id] = [cat, i_id_gr]
    
    fOut = open(path_out+fOutName, "a")
    print(i_id, c, cat, ttt, sep = "\t", file = fOut)
    fOut.close()
    
    if ttt == []:
        pt = "-"
    else:
        pt = ttt[0][0]

    st = st + "\t" + pt

    
    if c > 0:
        cc += 1

#print(st, file = fOut1)  
print(cc)

#fOut1.close()






