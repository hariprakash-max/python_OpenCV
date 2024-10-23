import cv2
import numpy as np
# import pygame
# pygame.mixer.init()
# sound = pygame.mixer.Sound("./")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
is_drinking = False

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        mouth_roi = gray[y + h // 2:y + h, x:x + w]
        _, mouth_thresh = cv2.threshold(mouth_roi, 50, 255, cv2.THRESH_BINARY)
        white_pixels = np.sum(mouth_thresh == 255)

        if white_pixels > 10000:
            if not is_drinking:
                print("Drinking coffee detected!")
                is_drinking = True
        else:
            is_drinking = False

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)