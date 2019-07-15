import cv2
from random import*
import os


directory = "C:\\Users\Cyril Tom Mathew\Desktop\images_test"
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        image = cv2.imread(os.path.join(directory, filename))
        face_cascade = cv2.CascadeClassifier("C:\\Users\Cyril Tom Mathew\Desktop\haarcascade_frontalface_default.xml")

        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_img, 1.38, 5)


        for (x, y, w, h) in faces:
            img_face = image[y:y+h, x:x+w]
            file_name = randrange(1000)
            cv2.imwrite("C:\\Users\Cyril Tom Mathew\Desktop\crop_faces\%s.png" %file_name, img_face)
