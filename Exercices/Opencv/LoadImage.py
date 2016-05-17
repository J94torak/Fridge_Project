import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('../../Pictures/code_barre.png',0)
cv2.imshow('ImageWindow',img)
cv2.waitKey(0)
cv2.destroyAllWindows()