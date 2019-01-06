import cv2
import os
import numpy as np

#This module resizes image from a given directory to 100*100 pixels and writes all images to given directory
count=0


for path, subdirnames, filenames in os.walk("./images"):

    for filename in filenames:
        # skiping the filename with '.'
        if filename.startswith("."):
            print("Skipping File:",filename)
            continue
        # the str(name) of path and filename
        img_path=os.path.join(path, filename)
        print("img_path",img_path)
        id=os.path.basename(path)

        #get the image or gif, resize(100,100)
        img = cv2.VideoCapture(img_path)
        success,img = img.read()
        if img is None:
            print("Image not loaded properly")
            continue
        resized_image = cv2.resize(img, (100, 100))
        new_path="./images"+"/"+str(id)
        # create a folder
        if os.path.exists(new_path):
            pass
        else:
            os.mkdir(new_path)
        print("desired path is",os.path.join(new_path, "frame%d.jpg" % count))
        # write imgs to the folder
        cv2.imwrite(os.path.join(new_path, "frame%d.jpg" % count),resized_image)
        count += 1
cv2.destroyAllWindows()
