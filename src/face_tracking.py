import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyautogui as robot



cam = cv2.VideoCapture(0)
screen_width, screen_height = robot.size()


base_path = os.path.dirname(__file__)  
cascade_path = os.path.join(base_path, "..", "cascades")

face_model = cv2.CascadeClassifier(os.path.join(cascade_path, "haarcascade_frontalface_default.xml"))
eye_model = cv2.CascadeClassifier(os.path.join(cascade_path, "haarcascade_eye.xml"))


loop = True
while loop:

    _ , image = cam.read()
    image = cv2.flip(image, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face = face_model.detectMultiScale(gray)

    if len(face) > 0:

        gray_face = gray [face[0][1] : (face[0][1] + face[0][3]) , face[0][0] : (face[0][0] + face[0][2]) ]
        eye = eye_model.detectMultiScale(gray_face , minSize = (30, 30))




        out =  cv2.rectangle(image, (face[0][0] , face[0][1]) , ( (face[0][0] + face[0][2]) , (face[0][1] + face[0][3]))  , (0, 255, 0) , 1)


        mouse_x , mouse_y = robot.position()
     

        white = (255, 255, 255)
        red = (0, 0, 255)
        rang = white


        if face[0][0] < 200:
            rang = red
            mouse_x = mouse_x - 20
            robot.moveTo(mouse_x , mouse_y , 0.1)
        if face[0][0] + face[0][2] > 450:
            rang = red
            mouse_x = mouse_x + 20
            robot.moveTo(mouse_x , mouse_y , 0.1)
        if face[0][1] < 100:
            rang = red
            mouse_y = mouse_y - 20
            robot.moveTo(mouse_x , mouse_y , 0.1)
        if face[0][1] + face[0][3] > 350:
            rang = red
            mouse_y = mouse_y + 20
            robot.moveTo(mouse_x , mouse_y , 0.1)




        out = cv2.rectangle(image , (200 , 100) , (450 , 350) , rang , 2)





        ice = 0
        for (x, y, w, h) in eye:
            ice += 1
            cv2.rectangle(image, ( (x + face[0][0]), (y + face[0][1])), ((x + w + face[0][0]), (y + h + face[0][1])), (255, 0, 0), 1)
            if ice == 2:
                break


        cv2.imshow('image', out)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            loop = False
            break
    else:
        print("Face not found")





