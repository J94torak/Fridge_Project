import detect_CB
import numpy as np
import cv2
import detect_CB
from time import sleep
device=0
cap=cv2.VideoCapture(device)

while 1:
    code_barre=detect_CB.detect_CB(cap)
    #print("cdb="+code_barre)
    if code_barre !="NULL":
        print("cdb="+code_barre)
        sleep(1)