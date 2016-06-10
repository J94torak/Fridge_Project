import numpy as np
import time
import cv2
import os
import detect_lines
from cv2 import waitKey
import math
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter

device=0
cap=cv2.VideoCapture(device)
secs=10

while 1 :
    
     ret, dst = cap.read()
     #cv2.imshow("input", dst)
     #name='code_barre_diag.png'
     #source='../../Pictures/'+name
     #dst = cv2.imread(source)
     if ret==True:
         gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
         height, width = gray.shape[:2]
         lines=detect_lines.detect_lines(gray) 
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
                     
                print("coord="+str(coord))
            coord.sort(cmp=None, key=None, reverse=False)
            print("coord="+str(coord))
             
            listMax=[len(list(group)) for key, group in groupby(coord)]
            print("listMax="+str(listMax))
             
            inde=listMax.index(max(listMax))
             
            c=0
            for i in range(inde) :
                c=c+listMax[i]
             
            vect=coord[c+1]
             
            angle=math.degrees(-np.pi/2+phase(complex(vect[0],vect[1])))
            print(-np.pi/2+phase(complex(vect[0],vect[1])))
            print(round(angle))
            M=cv2.getRotationMatrix2D((width/2,height/2),round(angle),1.0)
            dst = cv2.warpAffine(dst,M,(width,height))
            
            
            
            
         filename='img_modifie.png'
         cv2.imwrite(filename,dst)
         commande='zbarimg '+filename
         print(commande)
         code_barre=os.popen(commande).read()
         code_barre=str(code_barre)
         i=-1
         i=code_barre.rfind('EAN-13:')
         print("i="+str(i))
         if i!=-1 :
             code_barre=code_barre.replace('EAN-13:','')
             time.sleep(3)
         else:
             i=code_barre.rfind('EAN-8:')
             if i!=-1 :
                 code_barre=code_barre.replace('EAN-8:','')
                 time.sleep(3)
            
         print('code_barre='+str(code_barre))
         #cv2.imshow('img',img)
         #cv2.imshow('dst',dst)
         cv2.waitKey(50)
         cv2.destroyAllWindows()        




