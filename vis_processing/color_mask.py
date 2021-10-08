import cv2
import os
import numpy as np
import PIL

#abspath = "/Users/johannpally/Documents/GitHub/HydraBot/vis_processing/hydra_sample_imgs/00049.jpg"
#remember we are in the vis_processing foder already
#PIL.Image.open(path)

path = os.getcwd() + "/hydra_sample_imgs/00054.jpg"
img = cv2.imread(path)
c_img = cv2.imread(path)

#==============GEOMETRY===================
# circle mask

ww, hh = img.shape[:2]
r = 173
xc = hh // 2
yc = ww // 2
cv2.circle(c_img, (xc - 10, yc + 2), r, (255, 255, 255), -1)
hsv_cir = cv2.cvtColor(c_img, cv2.COLOR_BGR2HSV)

l_w = np.array([0,0,0])
h_w = np.array([0,0,255])
result_mask = cv2.inRange(hsv_cir, l_w, h_w)

#===============COLORS====================
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#(hMin = 7 , sMin = 66, vMin = 124), (hMax = 19 , sMax = 255, vMax = 237)
# Threshold of orange in HSV space
l_orange = np.array([7, 66, 125])
h_orange = np.array([19, 255, 240])
orange_mask = cv2.inRange(hsv_img, l_orange, h_orange)
orange_res = cv2.bitwise_and(img, img, mask = orange_mask)

#Threshold of black in HSV
l_black = np.array([0,0,0])
h_black = np.array([360,255,50])
black_mask = cv2.inRange(hsv_img, l_black, h_black)
black_res = cv2.bitwise_and(img, img, mask=black_mask)

for i in range(len(result_mask)):
    for j in range(len(result_mask[i])):
        if result_mask[i][j] == 255 & orange_mask[i][j] == 255:
            result_mask[i][j] = 255
        else:
            result_mask[i][j] = 0

c_o_res = cv2.bitwise_and(img, img, mask=result_mask)
cv2.imshow('res', c_o_res)
cv2.waitKey(0)
cv2.destroyAllWindows()