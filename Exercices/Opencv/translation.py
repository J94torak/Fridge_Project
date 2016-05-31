import numpy as np
import cv2
import math
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter

def translation(partie):
    
    print(partie)
    print(len(partie))
    A=[[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
    B=[[0,1,0,0,1,1,1],[0,1,1,0,0,1,1],[0,0,1,1,0,1,1],[0,1,0,0,0,0,1],[0,0,1,1,1,0,1],[0,1,1,1,0,0,1],[0,0,0,0,1,0,1],[0,0,1,0,0,0,1],[0,0,0,1,0,0,1],[0,0,1,0,1,1,1]]
    C=[[1,1,1,0,0,1,0],[1,1,0,0,1,1,0],[1,1,0,1,1,0,0],[1,0,0,0,0,1,0],[1,0,1,1,1,0,0],[1,0,0,1,1,1,0],[1,0,1,0,0,0,0],[1,0,0,0,1,0,0],[1,0,0,1,0,0,0],[1,1,1,0,1,0,0]]
    X=[[1,0,1,1,0,0,0],[1,0,0,1,1,0,0],[1,1,0,0,1,0,0],[1,0,1,1,1,1,0],[1,1,0,0,0,1,0],[1,0,0,0,1,1,0],[1,1,1,1,0,1,0],[1,1,0,1,1,1,0],[1,1,1,0,1,1,0],[1,1,0,1,0,0,0]]
    i=0
    decryptage=[]
    code_pays=""
    while i<len(partie):
        number=partie[i:i+7]
        print(number)
        j=0
        find=False
        while j < len(A) :
            if number==A[j] :
                decryptage.append(j)
                find=True
                code_pays+="A"
                break
            j+=1
        if find == False :
            j=0
            while j < len(B) :
                if number == B[j] :
                    decryptage.append(j)
                    find=True
                    code_pays+="B"
                    break
                j+=1
        if find == False:
            j=0
            while j < len(C) :
                if number==C[j] :
                    decryptage.append(j)
                    find=True
                    code_pays+="C"
                    break
                j+=1
        if find == False:
            j=0
            while j < len(X) :
                if number==X[j] :
                    decryptage.append(j)
                    find=True
                    code_pays+="X"
                    break
                j+=1
        i+=7
     
    return decryptage, code_pays