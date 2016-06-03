import numpy as np
import cv2
import translation
import rotation_cb
import detect_lines
import draw_lines
import binarization
import ean


img = cv2.imread('../../Pictures/code_barre8.png')
dst=rotation_cb.rotation_cb(img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=draw_lines.draw_lines(img,detect_lines.detect_lines(img),False)
code_barre=binarization.binarization(gray,detect_lines.detect_lines(gray))
print("code barre="+str(len(code_barre)))
decryptage=ean.ean(code_barre)
print(decryptage)

cv2.imshow('img',img)
cv2.imshow('lines',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()




