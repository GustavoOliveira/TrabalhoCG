import cv2
import numpy as np

harCascade = cv2.CascadeClassifier("palm_v4.xml")

camera = cv2.VideoCapture(0)

while True:
    _, imagem = camera.read()
    cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

    mao = harCascade.detectMultiScale(cinza, 1.3, 5)
    for (x,y,w,h) in mao:
        cv2.rectangle(imagem, (x,y), (x+w,y+h), (0,255,255),2)

    cv2.imshow("Foto", imagem)

    k = cv2.waitKey(50)
    if k == 27:
        break

cv2.destroyAllWindows()
camera.release()