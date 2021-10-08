# used makesense.ai to do annotations for images
import os

path = os.getcwd() + "/Train/"
i = 0
for file in os.listdir(path):
    split = os.path.splitext(file)
    os.rename(path + file, path + str(i).zfill(2) + split[1])
    i += 1