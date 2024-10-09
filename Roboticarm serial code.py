
#pip install cvzone==1.1
#pip install serial or serialbject


#-----
#CODE 
#-----
#by Aman 
#---------------------------------------------------------------------------------------------------------------------------------------

import cv2
import cvzone

cap = cv2.VideoCapture(0) # Check it by puting value 1& 0
detector = cvzone.HandDetector(maxHands=1,detectionCon=0.7)
mySerial = cvzone.SerialObject("COM3" , 9600 , 1)
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList,bbox = detector.findPosition(img)
    if lmList:
        fingers=detector.fingersUp()
        mySerial.sendData(fingers)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)




