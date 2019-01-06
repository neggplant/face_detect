import cv2
import os
import numpy as np
import faceRecognition as fr


# This module is to test 
test_img=cv2.imread('./Test_Images/x.jpg')
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)

# train once, comment it
faces,faceID=fr.label_of_train('./images')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save('trainme.yml')


# face_recognizer=cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('trainme.yml')

name={1:"cq"}

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>37):#If confidence less than 37 then don't print predicted face text on screen
        continue
    fr.put_text(test_img,predicted_name,x,y)



resized_img=cv2.resize(test_img,(1000,1000))
cv2.imshow("face dtecetion tutorial",resized_img)
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows
