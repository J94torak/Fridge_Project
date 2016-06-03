import numpy as np
import cv2
import math
import detect_lines
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter
from ctypes.wintypes import DOUBLE

def binarization(gray,lines):

    sortPoint=[]
    for x1,y1,x2,y2 in lines[0]:
        sortPoint.append([x1,y1,x2,y2])
        
    sortPoint.sort(cmp=None, key=None, reverse=False)
    print(sortPoint)
    print(sortPoint[0])
    
    i=0
    diffP=[]
    while i<len(sortPoint)-1:
        diffP.append(abs(sortPoint[i][0]-sortPoint[i+1][0]))
        i+=1
        
    #minim=min(diffP)
    #print(minim)
    #dist=[]
    #i=0
    #while i<len(diffP):
    #     dist.append(int(diffP[i]/minim))
    #     i+=1
        
    #print("dist="+str(dist))
    
    print(diffP)
    diffPS=list(diffP)
    diffPS.sort(cmp=None, key=None, reverse=False)
    print(diffPS)
    
    listMax=[len(list(group)) for key, group in groupby(diffPS)]
    print(listMax)
    
    inde=listMax.index(max(listMax))
    
    c=0
    i=0
    for i in range(inde) :
        c=c+listMax[i]
    
    vect=diffPS[c+1]
    print(vect)

    i=0
    dist=[]
    print(diffP)
    while i<len(diffP):
         dist.append(int(round(diffP[i]/DOUBLE(vect))))
         i+=1
        
    print(dist)
   
    
    code_barre=[]
    print(sortPoint)
    print(len(sortPoint))
    #point=[]
    i=0
    length=len(sortPoint)
    print(len(dist))
    while i<length-1:
        x1=sortPoint[i][0]
        x2=sortPoint[i][2]
        y1=sortPoint[i][1]
        y2=sortPoint[i][3]
        x3=sortPoint[i+1][0]
        x4=sortPoint[i+1][2]
        y3=sortPoint[i+1][1]
        y4=sortPoint[i+1][3]
        j=0
        if(gray[int((y1+y3+y2+y4)/4)][int((x1+x3)/2)]<int(255/2)):
            while j<dist[i]:
                code_barre.append(1)
                j+=1
        else:
            while j<dist[i]:
                code_barre.append(0)
                j+=1
        i+=1
    
    print(len(code_barre))
    return code_barre