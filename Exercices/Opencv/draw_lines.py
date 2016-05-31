import numpy as np
import cv2
import math
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter

def draw_lines(img,lines,same_image):
    if same_image==False :
        height, width = img.shape[:2]
        blank_image = np.zeros((height,width,3), np.uint8)
    else :
        blank_image=img
    i=0
    for x1,y1,x2,y2 in lines[0]:
        i=i+1
        cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,255),1)
    return blank_image