import numpy as np
import cv2
import math
import detect_lines
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter

def rotation_cb(img):

#from matplotlib import lines

# Load an color image in grayscale

    
    height, width = img.shape[:2]
    lines=detect_lines.detect_lines(img)    
    coord=[]
    for x1,y1,x2,y2 in lines[0]:
        norme=abs(sqrt((x1-x2)^2+(y1-y2)^2))
        x0=(x1-x2)/norme
        x0=int(x0)
        y0=(y1-y2)/norme
        y0=int(y0)
        #cv2.line(vecteur_image,(0,0),20*x0,20*y0,(255,255,255),1)
        #print(int(round(x0)),int(round(y0)))
        coord.append([x0,y0])
        
    print(coord)
    coord.sort(cmp=None, key=None, reverse=False)
    print(coord)
    
    listMax=[len(list(group)) for key, group in groupby(coord)]
    print(listMax)
    
    inde=listMax.index(max(listMax))
    
    c=0
    for i in range(inde) :
        c=c+listMax[i]
    
    vect=coord[c+1]
    
    angle=math.degrees(-np.pi/2+phase(complex(vect[0],vect[1])))
    print(-np.pi/2+phase(complex(vect[0],vect[1])))
    print(round(angle))
    M=cv2.getRotationMatrix2D((width/2,height/2),round(angle),1.0)
    dst = cv2.warpAffine(img,M,(width,height))

    return dst