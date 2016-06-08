import numpy as np
import cv2
import os
import rotation_cb
from cv2 import waitKey

name='code_barre9.png'
source='../../Pictures/'+name
img = cv2.imread(source)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst=rotation_cb.rotation_cb(gray)
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
    code_barre=code_barre.replace('EAN-13','')
print('code_barre='+str(code_barre))
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()




