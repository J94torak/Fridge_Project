import numpy as np
import cv2
import math
from cmath import sqrt, phase
from itertools import groupby
from collections import Counter

def detect_lines(gray):
    
    
    edges2 = cv2.Canny(gray,150,150,apertureSize = 3)
    minLineLength = 10
    maxLineGap = 100
    lines = cv2.HoughLinesP(edges2,1,np.pi/360,90,minLineLength,maxLineGap)
    
    return lines