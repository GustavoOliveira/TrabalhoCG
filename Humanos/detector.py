import cv2
from imutils.object_detection import non_max_suppression
import imutils
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

camera = cv2.VideoCapture('human.mp4')
while True:
    frame = camera.read()[1]
    #frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, width=min(400, frame.shape[1]))
    rects, wights = hog.detectMultiScale(
        frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    rects = np.array([[x, y, x+w, y+h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.85)

    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        print("[INFO] {} pessoas detectadas".format(len(pick)))
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(10)
    if key == 27:
        break


cv2.destroyAllWindows()
