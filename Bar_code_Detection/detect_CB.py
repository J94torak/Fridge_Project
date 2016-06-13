import numpy as np
import cv2
import os
from cv2 import waitKey
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter
import math

#device=0
#cap=cv2.VideoCapture(device)
def detect_CB(cap):
        
    ret, dst = cap.read()
    code_barre="NULL"
    if ret==True:
        gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
        height, width = gray.shape[:2]
        lines=detect_lines(gray) 
        if (lines is not None) and len(lines[0])>4 :
                coord=[]
                for x1,y1,x2,y2 in lines[0]:
                    norme=abs(sqrt((x1-x2)^2+(y1-y2)^2))
                    if norme!=0 :
                        x0=(x1-x2)/norme
                        x0=int(x0)
                        y0=(y1-y2)/norme
                        y0=int(y0)
                        coord.append([x0,y0])
                         
                    #print("coord="+str(coord))
                coord.sort(cmp=None, key=None, reverse=False)
                #print("coord="+str(coord))
                 
                listMax=[len(list(group)) for key, group in groupby(coord)]
                #print("listMax="+str(listMax))
                 
                inde=listMax.index(max(listMax))
                 
                c=0
                for i in range(inde) :
                    c=c+listMax[i]
                 
                vect=coord[c+1]
                 
                angle=math.degrees(-np.pi/2+phase(complex(vect[0],vect[1])))
                #print(-np.pi/2+phase(complex(vect[0],vect[1])))
                #print(round(angle))
                M=cv2.getRotationMatrix2D((width/2,height/2),round(angle),1.0)
                dst = cv2.warpAffine(dst,M,(width,height))
                
                
                
                
        filename='img_modifie.png'
        cv2.imwrite(filename,dst)
        commande='zbarimg '+filename
        #print(commande)
        code_barre=os.popen(commande).read()
        code_barre=str(code_barre)
        i=-1
        i=code_barre.rfind('EAN-13:')
        #print("i="+str(i))
        if i!=-1 :
                 
                 #print(code_barre)
                 code_barre=code_barre.replace('EAN-13:','')
                 #print("length="+str(len(code_barre)))
                 #if code_barre[len(code_barre)-1]=="\0":
                 code_barre=code_barre[:len(code_barre)-1]
                 #print(code_barre)
                 if checksum(code_barre)==False:
                     code_barre="NULL"
                 
                 #time.sleep(3)
        else:
                 i=code_barre.rfind('EAN-8:')
                 if i!=-1 :
                     code_barre=code_barre.replace('EAN-8:','')
                    # if code_barre[len(code_barre)-1]=="\0":
                     code_barre=code_barre[:len(code_barre)-1]
                     if checksum(code_barre)==False:
                         code_barre="NULL"
                 else :
                    code_barre="NULL"
                     #time.sleep(3)
    return code_barre   
        
        
def detect_lines(gray):
    
    edges2 = cv2.Canny(gray,150,150,apertureSize = 3)
    minLineLength = 100
    maxLineGap = 40
    lines = cv2.HoughLinesP(edges2,1,np.pi/360,90,minLineLength,maxLineGap)
    return lines   

def checksum(cdb):
    x=0
    y=0
    z=0
    i=0
    a=0
    leng=len(cdb)
    #print(cdb)
    last_number=int(cdb[leng-1])
    while i<leng-1:
        a=i%2
        #print(a)
        if a==0:
            x+=int(cdb[i])
        else:
            y+=int(cdb[i])
        i+=1
    z = x +3*y
    #print("x="+str(x))
    #print("y="+str(y))
    m=(10-z%10)%10
    #print("Checksum="+str(m))
    return m==last_number 




