import numpy as np
import cv2
import math
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter
from ctypes.wintypes import DOUBLE
#from matplotlib import lines

# Load an color image in grayscale




img = cv2.imread('../../Pictures/code_barre3.png')
height, width = img.shape[:2]
blank_image = np.zeros((height,width,3), np.uint8)
blank_image2 = np.zeros((height,width,3), np.uint8)
vecteur_image=np.zeros((height,width,3), np.uint8)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,150,150,apertureSize = 3)
minLineLength = 10
maxLineGap = 100
lines = cv2.HoughLinesP(edges,1,np.pi/180,90,minLineLength,maxLineGap)
i=0
for x1,y1,x2,y2 in lines[0]:
    i=i+1
    cv2.line(blank_image,(x1,y1),(x2,y2),(255,255,255),1)

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

gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
edges2 = cv2.Canny(gray,150,150,apertureSize = 3)
minLineLength = 10
maxLineGap = 100
lines2 = cv2.HoughLinesP(edges2,1,np.pi/360,90,minLineLength,maxLineGap)

print(lines2)
for x1,y1,x2,y2 in lines2[0]:
   cv2.line(blank_image2,(x1,y1),(x2,y2),(255,255,255),1)



sortPoint=[]
for x1,y1,x2,y2 in lines2[0]:
    sortPoint.append([x1,y1,x2,y2])
    
sortPoint.sort(cmp=None, key=None, reverse=False)
print(sortPoint)
print(sortPoint[0])

i=0
diffP=[]
while i<len(sortPoint)-1:
    diffP.append(abs(sortPoint[i][0]-sortPoint[i+1][0]))
    i+=1
i=0  



minim=min(diffP)
print(minim)

print(diffP)
diffPS=list(diffP)
diffPS.sort(cmp=None, key=None, reverse=False)
print(diffPS)

listMax=[len(list(group)) for key, group in groupby(diffPS)]
print(listMax)

inde=listMax.index(max(listMax))

c=0
for i in range(inde) :
    c=c+listMax[i]

vect=diffPS[c+1]
print(vect)
i=0


dist=[]
while i<len(diffP):
     dist.append(int(diffP[i]/minim))
     i+=1
    
print("dist="+str(dist))

i=0
dist2=[]
print(diffP)
while i<len(diffP):
     dist2.append(int(round(diffP[i]/DOUBLE(vect))))
     i+=1
    
print(dist)
print(dist2)

dist=dist2

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

premier_num=code_barre[0:3]
code_barre_reverse=list(reversed(code_barre))
dernier_num=code_barre_reverse[0:3]
print(code_barre)
print(code_barre_reverse)


code_barre_ean13666=False
if dernier_num == [1,0,1] and premier_num ==[1,0,1] :
    code_barre_ean13666=True


    
A=[[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
B=[[0,1,0,0,1,1,1],[0,1,1,0,0,1,1],[0,0,1,1,0,1,1],[0,1,0,0,0,0,1],[0,0,1,1,1,0,1],[0,1,1,1,0,0,1],[0,0,0,0,1,0,1],[0,0,1,0,0,0,1],[0,0,0,1,0,0,1],[0,0,1,0,1,1,1]]
C=[[1,1,1,0,0,1,0],[1,1,0,0,1,1,0],[1,1,0,1,1,0,0],[1,0,0,0,0,1,0],[1,0,1,1,1,0,0],[1,0,0,1,1,1,0],[1,0,1,0,0,0,0],[1,0,0,0,1,0,0],[1,0,0,1,0,0,0],[1,1,1,0,1,0,0]]


cdb=code_barre
print(len(cdb))
if code_barre_ean13666 ==True :
    partie1=cdb[3:7*6+3]
    partie666=cdb[7*6+3:7*6+8]
    partie2=cdb[7*6+8:len(code_barre)-3]
    print(partie1)
    print(partie666)
    print(partie2)
    pb=False
    if partie666 !=[0,1,0,1,0] :
        pb=True
    print("partie666="+str(partie666))
partie=partie1
bon_sens=True
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
    i+=7
print(decryptage)
print(code_pays)
decryptage_partie1=decryptage

if code_pays=="BBBBBB" or code_pays=="CCCCCC" :
    bon_sens=False
    
premier_chiffre=["AAAAAAA","AABABB","AABBAB","AABBBA","ABAABB","ABBAAB","ABBBAA","ABABAB","ABABBA","ABBABA"]

k=0
for number in premier_chiffre :
    if number==code_pays :
        break
    k+=1    
print(k)
 
partie=partie2
bon_sens=True
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
    i+=7
print(decryptage)
print(code_pays)
decryptage_partie2=decryptage 


decryptage_total=list([k]+decryptage_partie1+decryptage_partie2)
decryptage_inverse=list(decryptage_total)
decryptage_inverse.pop()
decryptage_inverse.reverse()
impair=0
pair=0

print(decryptage_total[len(decryptage_total)-1])
print(decryptage_inverse)
l=0
while l< len(decryptage_inverse) :
    if l%2==0 :
        impair+=decryptage_inverse[l]
        print("decrypatge_impair="+str(decryptage_inverse[l]))
    else :
        pair+=decryptage_inverse[l]
        print("decrypatge_pair="+str(decryptage_inverse[l]))
    l+=1

print(pair)
print(impair)
checksum=(10-((3 * impair + pair)% 10))% 10

print(checksum)

print(decryptage_total)



#cv2.imwrite('houghlines5.jpg',blank_image)
#cv2.imshow('Edges2',edges2)
#cv2.imshow('Edges',edges)
cv2.imshow('Gray2',gray)
#cv2.imshow('Result1',blank_image)
cv2.imshow('Result2',blank_image2)
#cv2.imshow('Origin',img)
#cv2.imshow('Vecteurs',vecteur_image)
#cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()