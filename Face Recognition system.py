import cv2
face_cascade = cv2.CascadeClassifier('face_detector.xml') # load the cascade
img = cv2.imread('test1.jpg')  # read the input image
faces = face_cascade.detectMultiScale(img, 1.1, 4)  # detect faces
# draw rectangle around the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0),2)
# export the result
cv2.imwrite("face_detected.png", img)
print('photo successfully exported!')
