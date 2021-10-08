# Importing OpenCV library
import cv2, os


# user define function
# that return None or
def check_empty_img(img):
    # Reading Image
    # You can give path to the
    # image as first argument
    image = cv2.imread(img)

    # Checking if the image is empty or not
    if image is None:
        result = "Image is empty!!"
    else:
        result = "Image is not empty!!"

    return result

path = os.getcwd() + "/Train/"
for file in os.listdir(path):
    split = os.path.splitext(file)
    if split[1] != ".xml":
        print(file)
        print(check_empty_img(path+file))
