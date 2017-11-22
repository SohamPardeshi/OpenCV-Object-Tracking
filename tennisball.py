import numpy as np
import imutils
import cv2

screen = cv2.VideoCapture(0)

pressed = None
while pressed != ord("q"):
	(grabbed, frame) = screen.read()

	mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), (26, 23, 148), (65, 182, 255))
	contours = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
	((x, y), r) = cv2.minEnclosingCircle(max(contours, key=cv2.contourArea))
        threshold = 10

	if r > threshold and len(contours) > 0:
                center = (int(x), int(y))
		radius = int(r)
		color = (20, 255, 20)
		radius = 2

		cv2.circle(frame, center, radius, color, radius)

	frame = imutils.resize(frame, width=600)
	cv2.imshow("Tennis Balls", frame)
	pressed = cv2.waitKey(1)

screen.release()
cv2.destroyAllWindows()
