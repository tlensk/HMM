#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 08:55:05 2023

@author: tatianalenskaia
"""

import hmmout_parse_lib as hpl

path = "/Users/tatianalenskaia/HMM/Results/Rset_755phs/"
# Tab delimited with two column
fInName1 = "Pfam_hmm_list.txt"
d_p = hpl.Pfam_ver_lookup(path+fInName1)



path = "/Users/tatianalenskaia/HMM/All_HMMs/"
#fInName = "HMM-List_DavidsonForTatiana.csv"
fInName = "hmm_found_682_update.csv"
res = hpl.Aset_HMM_list_update(path+fInName)
t_hmm = res[-1]
d_hmm_aset = res[0]
d_cat = res[1]
d_spread = res[2]
d_cat_fun = res[3]




#====================================================

'''

path = "/Users/tatianalenskaia/_ShC_phages/Genomes/Outliers/17Kb/"
fInName = "MK433583_cds.faa"

label = "MK433583"
ftype = "faa"
'''


'''
path = "/Users/tatianalenskaia/_ShC_phages/Genomes/Representatives/AH07/"
fInName = "MZ501270.1(AH07)_aa.txt"

label = "MZ501270"
ftype = "aa"
'''



path = "/Users/tatianalenskaia/_ShC_phages/230601_Clustering/HMM_res/"
fInName = "312phages_cds.faa"

label = "312phages"
ftype = "faa"





path = "/Users/tatianalenskaia/UT/Karen/Pa_phs_acr/"
fInName = "1252paphs_aa.faa"

label = "1252paphs"
ftype = "aa"





path = "/Users/tatianalenskaia/UT/Charles_phages/All_phages_080123/All_phage_genomes/hmm_res/"
fInName = "12phages_cds.faa"

label = "12phages"
ftype = "faa"




path = "/Users/tatianalenskaia/_ShC_phages/Genomes/GenBank_accession_081323/HMM_res/"
fInName = "312phages_cds_update.faa"

label = "312phages"
ftype = "faa"



path = "/Users/tatianalenskaia/_ShC_phages/Genomes/GenBank_accession_081323/Lambda_HK97/"
fInName = "Lambda_HK97_cds.faa"

label = "LHK"
ftype = "faa"


path = "/Users/tatianalenskaia/_ShC_phages/Genomes/GenBank_accession_081323/five_others/"
fInName = "NC_015295_cds.faa"

label = "fiveothers"
ftype = "faa"


path = "/Users/tatianalenskaia/_ShC_phages/Genomes/GenBank_accession_081323/Update_L_genome/"
fInName = "MW013503_cds.faa"


label = "L"
ftype = "faa"



'''

path = "/Users/tatianalenskaia/HMM/755phs/"
fInName = "755phs_cds_seq.faa"

label = "755"
ftype = "aa"





path = "/Users/tatianalenskaia/_ShC_phages/Genomes/GenBank_accession_081323/3_HMM_res/"
fInName = "312phages_cds_update.faa"

label = "312HO"
ftype = "faa"

'''

'''
fInName = "NZ_CP007470_cds.faa"
fInName = "ON041214.1_sequence_aa.txt"


fInName = "mmseqs2_3129098_0.8_0.8_cls.out"
'''


res_cds = hpl.ReadSeqCDS(path+fInName, ftype = ftype)
d_pid = res_cds[0]
print(len(d_pid))



#====================================================

path_out = "/Users/tatianalenskaia/HMM/All_HMMs/"
path_out = "/Users/tatianalenskaia/_ShC_phages/230601_Clustering/MMseq2/0.8_0.8/HMM_results/"

#path_out = "/Users/tatianalenskaia/_ShC_phages/HO-PG-IN/PAT_HO/"

path_out = path

t_list = ["Aset_Custom_b.out",
          "Aset_Custom_f.out",
          "Pfam-A.out",
          "TIGRFAM_release15.out"]



#t_list = ["Aset_Custom_b.out"]

#t_list = ["PAT_HO_all.out"]

#---------- Read-in hmm.out files

hmm_res = hpl.ReadInHMMout(path_out, t_list, d_pid,ftype)

d_hmm_res = hmm_res[0]
d_hmm_prs = hmm_res[1]

#-----------------------------------




#print(len(t_hmm))

fOutName = label+"_phages_HMMres_PAT.txt"
fOut = open(path_out+fOutName, "w")
#print("Genome_id|Protein_id",	"Location", "Initial_annotation","Number_of_HMM_hits","Category", "Details_about_HMM_hits [category,function, hmm_id, hmm_accession, hmm_name, e-value]", sep = "\t", file = fOut)

print("Genome_id|Protein_id", "Number_of_HMM_hits","Category", "Details_about_HMM_hits [category,function, hmm_id, hmm_accession, hmm_name, e-value, start_pos, end_pos, aligned]", sep = "\t", file = fOut)
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
                pos_st = item[-3]
                pos_fn = item[-2]
                s = item[-1]
                lb = ""
                fn = ""
                if hmm in d_hmm_aset:
                    lb = d_hmm_aset[hmm][0]
                    fn = d_cat_fun[lb]
                    if fl_pat == 0:
                        i_id_gr = fn
                        cat = lb
                        fl_pat = 1
                #ttt.append([lb]+[fn]+item[0:4])
                ttt.append([lb]+[fn]+item)
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








