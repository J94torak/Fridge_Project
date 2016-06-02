import numpy as np
import cv2
import math
import detect_lines
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter
import translation

def ean(code_barre):


    premier_num=code_barre[0:3]
    code_barre_reverse=list(reversed(code_barre))
    dernier_num=code_barre_reverse[0:3]
    print(code_barre)
    print(code_barre_reverse)
    
    
    code_barre_ean666=False
    if dernier_num == [1,0,1] and premier_num ==[1,0,1] :
        code_barre_ean666=True
    
    cdb=code_barre
    length=len(cdb)
    print(length)
    pb=False
    ean13=True
    decryptage_total=[]
    if code_barre_ean666 == True :
        if length==95 :
            partie1=cdb[3:7*6+3]
            partie666=cdb[7*6+3:7*6+8]
            partie2=cdb[7*6+8:length-3]
        else:
            if length==67:
                    ean13=False
                    partie1=cdb[3:7*4+3]
                    partie666=cdb[7*4+3:7*4+8]
                    partie2=cdb[7*4+8:length-3]
        print("partie1="+str(partie1))
        print("partie666="+str(partie666))
        print("partie2="+str(partie2))
        pb=False
        if partie666 !=[0,1,0,1,0] :
            print("partie666="+str(partie666))
            pb=True
        else:
            decryptage1, code_pays1=translation.translation(partie1)
            decryptage2, code_pays2=translation.translation(partie2)
            print("decryptage1="+str(decryptage1))
            print("decryptage2="+str(decryptage2))
            print("code_pays1="+str(code_pays1))
            print("code_pays2="+str(code_pays2))
            if pb==False and ean13==True:
                if (code_pays2 =="BBBBBB" or code_pays2 =="CCCCCC") and (code_pays1 !="BBBBBB" and code_pays1 !="CCCCCC") :
                     decryptage_total=list([nombre_pays(code_pays1)]+decryptage1+decryptage2)
                else:  
                    if  (code_pays1 =="BBBBBB" or code_pays1 =="CCCCCC") and (code_pays2 !="BBBBBB" and code_pays2 !="CCCCCC") :
                        decryptage_total=list(decryptage1+decryptage2+[nombre_pays(code_pays2)])
                        decryptage_total.reverse()
                    else :
                        print("ERROR: Probleme code barre Pays")
            else :        
                if pb==False and ean13==False:
                    if code_pays1=="AAAA" and code_pays2=="CCCC":
                        decryptage_total=decryptage1+decryptage2
                    if code_pays2=="AAAA" and code_pays1=="CCCC":
                        decryptage_total=decryptage1+decryptage2
                        decryptage_total.reverse()
                    if code_pays2=="XXXX" and code_pays1=="BBBB":
                        decryptage_total=decryptage1+decryptage2
                        decryptage_total.reverse()   
                    else: print("ERROR: Probleme partie code barre")
                else: print("ERROR: Probleme partie code barre")
            
            
    return decryptage_total

def nombre_pays(code_pays):
    
    premier_chiffre=["AAAAAAA","AABABB","AABBAB","AABBBA","ABAABB","ABBAAB","ABBBAA","ABABAB","ABABBA","ABBABA"]
    premier_chiffre2=["XXXXXX","CCXCXX","CXCCXX","XCCCXX","CCXXCX","CXXCCX","XXCCCX","CXCXCX","XCCXCX","XCXCCX"]

    k=0
    for number in premier_chiffre :
        if number==code_pays :
            break
        k+=1
    if k==10:
        k=0
        for number in premier_chiffre2 :
            if number==code_pays :
                break
            k+=1   
    print(k)
    
    return k