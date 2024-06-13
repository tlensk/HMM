# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:12:26 2023

@author: tilen


Updated on Jan 13 2023

One more column is added to the output info file to record the name of Pfam HMMs

Two output files are now generated.


"""


import core_methods as cm


path = "/Users/tatianalenskaia/HMM/755phs/"
path="/Users/tatianalenskaia/_ShC_phages/HO-PG-IN/"

d = {}
#fInName = "Rset_Pfam_462.txt"

fInName = "Pfam_aPAT_ST.txt"
fInName="Pfam_PAT_HO.txt"





path = "/Users/tatianalenskaia/HMM/All_HMMs/HMM_db/"
fInName = "A_IN.txt"




'''

fIn = open(path+fInName,"r")
lines = fIn.readlines()
for line in lines:
    line = line.strip()
    name = line.split(".")[0]
    if name not in d:
        d[name] = line
        
print(len(d))
#print(name, d[name])
fIn.close()

'''

d_p = {}
path1 = "/Users/tatianalenskaia/HMM/755phs/"
fInName1 = "Pfam_hmm_list.txt"


path1 = "/Users/tatianalenskaia/HMM/All_HMMs/HMM_db/"
fInName1 = "A_IN.txt"


fIn = open(path1+fInName1,"r")
lines = fIn.readlines()
for line in lines:
    line = line.strip()
    hmm = line.split("\t")[0]
    name = hmm.split(".")[0]
    desc = line.split("\t")[1]
    if name not in d_p:
        d_p[name] = [hmm, desc]
    else:
        print("duplicate!")
        
print(len(d_p))
#print(name, d_p[name])
fIn.close()



sep = "\t"
fOutName = fInName.split(".")[0]+"_update_info.txt"
fOut = open(path+fOutName,"w")
fOut.write("Pfam_id"+sep+"Pfam_release35"+sep+"Pfam_PAT_Rset"+sep+"Pfam_name"+"\n")



for it in d:
    if it in d_p:
        fOut.write(it+sep+d_p[it][0]+sep+d[it]+sep+d_p[it][1]+"\n")
        
        
fOut.close()    




fOutName = fInName.split(".")[0]+"_update.txt"
fOut = open(path+fOutName,"w")
for it in d:
    if it in d_p:
        fOut.write(d_p[it][0]+"\n")
        
        
fOut.close()       

   