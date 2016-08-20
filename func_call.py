import cv2
import os

imageformat=".PNG"
path="C:\Users\Riya\Desktop\Drone\Test Bench"
imfilelist=[os.path.join(path,f) for f in os.listdir(path) if f.endswith(imageformat)]
for el in imfilelist:
        print el
        image = cv2.imread(el)
        cv2.imshow('Image', image) #Show the image
        cv2.waitKey(1000)