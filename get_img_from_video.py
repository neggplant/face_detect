
# getting some images from camera
import cv2

# path of saving
path = './images/01/'

cap=cv2.VideoCapture(0)

count = 0
while True:
    ret,test_img=cap.read()
    if not ret :
        continue
    cv2.imwrite(path + "frame%d.jpg" % count, test_img)     # save frame as JPG file
    count += 1
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    if cv2.waitKey(100) == "q":
        break


cap.release()
cv2.destroyAllWindows
