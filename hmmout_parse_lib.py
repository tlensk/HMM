#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 08:49:30 2023

@author: tatianalenskaia
"""

import core_methods as cm
import copy as cp


#path = "/Users/tatianalenskaia/HMM/755phs/"
#fInName = "755phs_cds_seq.faa"


#path = "/Users/tatianalenskaia/HMM/Results/755phs_cds/"
#fInName = "NC_009799.3_cds.faa"


#path = "/Users/tatianalenskaia/HMM/Results/Rset_755phs/"


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


def HighlightAlign(seq, st, fn):
    # This snippet highlights the aligned part of the sequence
    n = len(seq)
    st = st-1
    fn= fn-1
    
    s = ""
    for i in range(n):
        if (i <= st) or (i >= fn):
            s = s+"."
        else:
            s = s+seq[i]
    return s




def Aset_HMM_list(fInName):
    # The snippet reads in the list of HMMs shared that are prioritized
    # and creates three dictionaries: dd, d_cat, and d1
    # dd: key hmm_id value [hmm_cat, hmm_name, hmm_Pfam_def, hmm_func, hmm_spread]
    # d_cat: key category value []
    # d1: 
        
    
    '''
    dd [HMMs in Alan's list of priorities']:
    
    
    '''    
    
    
    
        
        
    '''
    d1 [functional category spread among phages]:
        
    All tailed phages                       10  ['ST', 'LT', 'LW', 'PO', 'S7', 'HP', 'HS', 'HD', 'MH', 'PC']
    Long-tailed phages                      8   ['C1', 'C2', 'TC', 'TR', 'TT', 'TG', 'TH', 'TM']
    Gram-negative siphophage                5   ['LM', 'LL', 'LK', 'LI', 'CF']
    Gram-positive siphophage                4   ['DT', 'BH', 'BL', 'XL']
    Myophage                                8   ['DL', 'BD', 'BS', 'BW', 'BJ', 'BI', 'TS', 'UA']
    not phage-specific                      1   ['IN']
    Gram-positive siphophage and myophage   1   ['XL']
    Myophage| T6SS| PVC                     1   ['SE']
    (blank)                                 1   ['XI']

    '''    
    
    
    '''
    All tailed phages ST 19
    All tailed phages LT 7
    All tailed phages LW 4
    All tailed phages PO 14
    All tailed phages S7 7
    All tailed phages HP 17
    All tailed phages HS 17
    All tailed phages HD 12
    All tailed phages MH 34
    All tailed phages PC 9
    
    '''
    
    
    
    
    
    
    
    
    
    
    ttt = ["PF08932.5"]    
    
    
    fIn = open(fInName, "r")
    lines = fIn.readlines()
    fIn.close()
    
    
    header = lines[0]
    lines = lines[1:]
    
    # Dicctionary of HMMs
    dd = {}
    
    d_cat = {}
    
    d_cat_fun = {}
    
    d1 = {}
    
    tt_Ahmm = []
    
    for line in lines:
        line = line.strip()
        t_line = line.split(",")
    
    
        
        hmm_cat = t_line[0]
        hmm_name = t_line[1]
        hmm_acc = t_line[2]
        hmm_Pfam_def = t_line[3]
        
        hmm_func =  t_line[5]
        hmm_spread = t_line[6]
        hmm_focus = t_line[7]
        
        
        # Update Pfam versions
        hmm_id = hmm_acc
        if (hmm_id[0:2] == "PF") and (hmm_id != "PF08932.5"):
            hmm_id = d_p[hmm_id.split(".")[0]][0]
        
        
        # Update Pfam version
        
        
        
        
        
        if (hmm_focus == "yes") and (hmm_id not in ttt):
            
            
            
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
        
            
        
    '''   
    print(len(d_cat))
    
    for it in d_cat:
        print(it, len(d_cat[it]))
    
    print(d1)
    '''

    
    return [dd, d_cat, d1, d_cat_fun]





def ReadSeqCDS(fInName, ftype = "aa"):
    # the keys in d dictionary should match the names of the sequences in the first column of the .out file
    
    i = 0
    tt = []
    
    
    d = {}
    d_pid = {}
    
    t_id = []
    t_pid = []
    
 
    
    fIn = open(fInName, "r")
    for line in fIn:
        line = line.strip()
        i = i+1

        if (line != "") and (line[0] == ">"):
            if tt != []:    
                
                if ftype == "faa":
                    ln = tt[0]
                    
                    t_ln = ln[1:].split("|")
                    
                    g_acc = t_ln[0]
                    pid = t_ln[1]
                    '''
                    pr = t_ln[2]
                    loc = t_ln[3]
                    p_sz = t_ln[4].split()[0]
                    '''
                    i_id = g_acc+"|"+pid

                if ftype == "aa":
                    ln = tt[0]
                    t_ln = ln[1:].split()
                    nm = t_ln[0].split("|")[1]
                    t_nm = nm.split("prot")
                    #print(t_nm)
                    g_acc = t_nm[0][0:-1]
                    pid = t_nm[-1].rsplit("_",1)[0][1:]
                    p_num = t_nm[-1].rsplit("_",1)[-1]
                    
                    if pid == "":
                        print(ln)
                        print(p_num)
                    
                    i_id = nm
                    
                    
                    
                seq = ""
                for item in tt[1:]:
                    seq = seq+item


                #print(g_acc, pid)
                
                
                '''
                t_id.append(i_id)
                t_pid.append(pid)

                    
                    
                if g_acc not in d:
                    d[g_acc] = []
                d[g_acc].append(pid)
                
                if pid not in d_pid:
                    d_pid[pid] =[]
                else:
                    print("duplicate",pid)
                #d_pid[pid] = [g_acc,pr, loc, p_sz, seq]
                d_pid[pid] = [g_acc]
                '''
                
                if i_id not in d:
                    d[i_id] = [seq]
                else:
                    print("duplicate")


                
                tt = []

        tt.append(line)
        
        
    
    
    if tt != []:
        if ftype == "faa":
            ln = tt[0]
            t_ln = ln[1:].split("|")
            
            g_acc = t_ln[0]
            pid = t_ln[1]
            '''
            pr = t_ln[2]
            loc = t_ln[3]
            p_sz = t_ln[4].split()[0]

            '''
            i_id = g_acc+"|"+pid
            
        if ftype == "aa":
            ln = tt[0]
            t_ln = ln[1:].strip().split()
            nm = t_ln[0].split("|")[1]
            t_nm = nm.split("prot")
            #print(t_nm)
            g_acc = t_nm[0][0:-1]
            pid = t_nm[-1].rsplit("_",1)[0][1:]
            i_id = nm
        


        seq = ""
        for item in tt[1:]:
            seq = seq+item



        '''
        t_id.append(i_id)  
        t_pid.append(pid)
        
        seq = ""
        for item in tt[1:]:
            seq = seq+item
            
        if g_acc not in d:
            d[g_acc] = []
        d[g_acc].append(pid)
        
        if pid not in d_pid:
            d_pid[pid] =[]
        else:
            print("duplicate",pid)
        #d_pid[pid] = [g_acc,pr, loc, p_sz, seq]
        d_pid[pid] = [g_acc]
        '''

        if i_id not in d:
            d[i_id] = [seq]
        else:
            print("duplicate")

        
        
    print("d", len(d))
        
    return [d]




def Aset_HMM_list_update(fInName):
    
    
    
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
    
    
    t_hmm = []
    
    #sp2 = ","
    #fOut1 = open("/Users/tatianalenskaia/HMM/All_HMMs_cases/hmm_found_yesmaybe.csv", "w")
    #fOut1.write(header.strip()+sp2+"HMM_file"+"\n")
    
    for line in lines:
        line = line.strip()
        t_line = line.split(",")
        #print(t_line)
        
      
    
        
        if len(t_line) != 11:
            print(len(t_line), t_line)
            break
    
        
        hmm_cat = t_line[0]
        hmm_name = t_line[1]
        hmm_acc = t_line[2]
        hmm_Pfam_def = t_line[3]
        
        hmm_func =  t_line[5]
        hmm_spread = t_line[6]
        hmm_focus = t_line[7]
        
        hmm_file = t_line[-1]
        
        
        t_hmm.append(hmm_file)
        
        '''
        # Update Pfam versions
        hmm_id = hmm_acc
        if (hmm_id[0:2] == "PF") and (hmm_id != "PF08932.5"):
            hmm_id = d_p[hmm_id.split(".")[0]][0]
        
        '''
        
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
                    
            
            
        
            
            
            
        # Creating a dictionary of HMMs
        if hmm_file not in dd:
            dd[hmm_file] = [hmm_cat, hmm_name, hmm_Pfam_def, hmm_func, hmm_spread]
            tt_Ahmm.append(hmm_file)
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
            """
            
        
    '''   
    print(len(d_cat))
    
    for it in d_cat:
        print(it, len(d_cat[it]))
    
    print(d1)
    '''
    print(ct, cc)
    
    print(c_acc, c_name, c_Pfam, c_pf_tg, c_0)
    #fOut1.close()
    
    return [dd, d_cat, d1, d_cat_fun, t_hmm]








def ReadInHMMout(path_out, t_list, d_pid, ftype):

    d_hmm_prs = {}
    d_hmm_res = {}
    
    
    for it in t_list:
        
        #fInName = "PF11123.11.out"
        #fInName = it+".out"
        fInName = path_out+it
        
        
        
        #fIn = open(path+fInName, "r")
        fIn = open(fInName, "r")
        lines = fIn.readlines()
        for line in lines:
            
            if line[0] != "#":
                line = line.strip()
                t_line = line.split()
                ln = t_line[0]
                
    
                hmm_acc = t_line[4]
                hmm_name = t_line[3]
                
                hmm_id = hmm_acc
                if hmm_acc == "-":
                    hmm_id = hmm_name
    
    
                e = float(t_line[6])
                
                pos_st = int(t_line[17])
                pos_fn = int(t_line[18])
    

                
            
                if ftype == "faa":
                    t_ln = ln.split("|")
                    i_id = t_ln[0]+"|"+t_ln[1]
                if ftype == "aa":
                    t_ln = ln.split("|")
                    i_id = t_ln[-1]
                
                s_align = HighlightAlign(d_pid[i_id][-1], pos_st, pos_fn)
                #s_align = ""
                
                print(i_id)
                
                
                
                
                
               #s_align = HighlightAlign(d_pid[pid][-1], pos_st, pos_fn)
                
                #print(s_align)
                
                if hmm_id not in d_hmm_res:
                    d_hmm_res[hmm_id] = []
                d_hmm_res[hmm_id].append([i_id,e, pos_st, pos_fn, s_align])
                
                if i_id not in d_hmm_prs:
                    d_hmm_prs[i_id] = []
                d_hmm_prs[i_id].append([hmm_id, hmm_acc, hmm_name, e, pos_st, pos_fn, s_align])
                
                
                #break
                
    
                
                
            
        fIn.close()
        
    return [d_hmm_res, d_hmm_prs]















