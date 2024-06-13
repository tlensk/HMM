#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:31:49 2023

@author: tatianalenskaia
"""



import core_methods as cm

def Pfam_ver_lookup(fInName1):
    # The snippet read in the list of HMMs in Pfam release 35 
    #and creates d_p dictionary of Pfams for version look-up
    # 19632 HMMs in total in d_p
    # d_p: key PF00569 value ['PF00569.20', 'ZZ']

    d_p = {}
    
    fIn = open(fInName1,"r")
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
            
    #print(len(d_p))
    #print(name, d_p[name])
    fIn.close()
    
    return d_p

def Aset_HMM_list_update(fInName, t_hmm):
    
    
    ttt = ["PF08932.5"]    
    
    
    fIn = open(fInName, "r")
    lines = fIn.readlines()
    fIn.close()
    
    
    header = lines[0]
    lines = lines[1:]
    
    #print(len(lines))
    
    dd = {}
    
    d_cat = {}
    
    d_cat_fun = {}
    
    d1 = {}
    
    tt_Ahmm = []

    ct = 0
    cc = 0
    
    c_0 = 0
    c_acc = 0
    c_name = 0
    c_Pfam = 0
    c_pf_tg = 0
    
    sp2 = ","
    fOut1 = open("/Users/tatianalenskaia/HMM/All_HMMs_cases/hmm_found_yesmaybe.csv", "w")
    fOut1.write(header.strip()+sp2+"HMM_file"+"\n")
    
    for line in lines:
        line = line.strip()
        t_line = line.split(",")
        #print(t_line)
        
      
    
        
        if len(t_line) != 10:
            print(len(t_line), t_line)
            break
    
        
        hmm_cat = t_line[0]
        hmm_name = t_line[1]
        hmm_acc = t_line[2]
        hmm_Pfam_def = t_line[3]
        
        hmm_func =  t_line[5]
        hmm_spread = t_line[6]
        hmm_focus = t_line[7]
        
        '''
        # Update Pfam versions
        hmm_id = hmm_acc
        if (hmm_id[0:2] == "PF") and (hmm_id != "PF08932.5"):
            hmm_id = d_p[hmm_id.split(".")[0]][0]
        
        '''
    
        hmm_file = ""  
        
        #if ((hmm_focus == "yes") or (hmm_focus == "maybe")) and (hmm_id not in ttt):
        if ((hmm_focus == "yes") or (hmm_focus == "maybe")): 
        #if ((hmm_focus == "yes") or (hmm_focus == "maybe")) :
            
            ct += 1
            
            #'U_LW_Brady', 'U_LW_Fam2'
            #if (hmm_acc in t_hmm) and (hmm_name in t_hmm) and (hmm_name == hmm_acc):
            #if (hmm_acc in t_hmm):
                
              
            if (hmm_acc in t_hmm):
                c_acc += 1
                hmm_file = hmm_acc
            else:
    
                if (hmm_acc[0:2] == "PF") or (hmm_acc[0:4] == "TIGR"):
                    if hmm_acc[0:2] == "PF":
                        hmm = hmm_acc.split(".")[0]
                        if hmm in d_p:
                            hmm_file = d_p[hmm][0]
                    if hmm_acc[0:4] == "TIGR":     
                        hmm_file = hmm_acc
                    c_pf_tg += 1
                else:         
                    if hmm_name in t_hmm:
                        c_name += 1
                        hmm_file = hmm_name
                    elif hmm_Pfam_def in t_hmm:
                        c_Pfam += 1
                        hmm_file = hmm_Pfam_def 
                    else:
                        c_0 += 1
                    
            '''        
            if (hmm_acc != hmm_Pfam_def) and (hmm_Pfam_def in t_hmm):
            if (hmm_acc != hmm_Pfam_def) and (hmm_Pfam_def in t_hmm):
                print(hmm_Pfam_def)
                fl = 1
                cc += 1
            '''
            
            
            
        
            
            """
            
            # Creating a dictionary of HMMs
            if hmm_id not in dd:
                dd[hmm_id] = [hmm_cat, hmm_name, hmm_Pfam_def, hmm_func, hmm_spread]
                tt_Ahmm.append(hmm_id)
            else:
                print(hmm_acc, "duplicate!")
             
                
            # Creating a dictionary of categories
            if hmm_cat not in d_cat:
                d_cat[hmm_cat] = []
            d_cat[hmm_cat].append(hmm_acc)


            # Creating a dictionary of category spread 
            # (what scope of phages has this function)            
            if hmm_spread not in d1:
                d1[hmm_spread] = []
            if hmm_cat not in d1[hmm_spread]:
                d1[hmm_spread].append(hmm_cat)
                
                
            if hmm_cat not in d_cat_fun:
                d_cat_fun[hmm_cat] = hmm_func
            """
            if hmm_file != "":
                fOut1.write(sp2.join(t_line)+sp2+hmm_file+"\n")
            
        
    '''   
    print(len(d_cat))
    
    for it in d_cat:
        print(it, len(d_cat[it]))
    
    print(d1)
    '''
    print(ct, cc)
    
    print(c_acc, c_name, c_Pfam, c_pf_tg, c_0)
    fOut1.close()
    
    return [dd, d_cat, d1, d_cat_fun]





path = "/Users/tatianalenskaia/HMM/All_HMMs/"
fInName = "Custom_HMM_list.txt"
t = cm.GetListFromFile(path+fInName)


t_hmm = []
for it in t:
    t_hmm.append(it.split(".")[0])
print("all_custom",len(t_hmm))


path = "/Users/tatianalenskaia/HMM/Results/Rset_755phs/"

# Tab delimited with two column
fInName1 = "Pfam_hmm_list.txt"
d_p = Pfam_ver_lookup(path+fInName1)



path = "/Users/tatianalenskaia/HMM/From Alan/"

# BL	DUF1914	PF08932.5	Domain of unknown function (DUF1914)		Receptor binding proteins	Gram-positive siphophage	yes	1	BL	DUF1914	PF08932.5	Domain of unknown function (DUF1914)		Receptor binding proteins	Gram-positive siphophage	yes	1	
# Coma delimited with 10 columns
fInName = "HMM-List_Tatiana_Update.csv"
res = Aset_HMM_list_update(path+fInName, t_hmm)



