import cv2,os

path = os.getcwd() + "/Train/"
for file in os.listdir(path):
    #split = os.path.splitext(file)
    im = cv2.imread(path+file)
    print(im.shape)