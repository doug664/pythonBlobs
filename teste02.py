import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('simples.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

__,img_bin = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Binario invertido', img_bin)

cv2.waitKey(0)
cv2.destroyAllWindows()