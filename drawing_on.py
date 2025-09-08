import cv2
import cvzone
import numpy as np 

# importtin the model :
from cvzone.HandTrackingModule import HandDetector
#instantiation :
detector = HandDetector(detectionCon=0.5, maxHands=1,minTrackCon=0.5)
#the code main function:
def functional(frame,canvas):
    if canvas is None:
        canvas=np.zeros_like(frame)#our canva we will be drawing in 
    hands, img = detector.findHands(frame, draw=True)#hands[0]["lmList"] has the 21 list of coordinates 
    h, w, _ = img.shape
    if hands:
        hand = hands[0]  # Get the first hand
        landmarks = hand["lmList"]  # List of 21 landmark points
        #each landmark store three vars [x, y,id]
        index_tip = landmarks[8]
        x,y,_=index_tip

        #visulaizing where the index is :
        cv2.circle(img,(int(x),int(y)),15,(255, 20, 147),cv2.FILLED)
        cv2.circle(canvas,(int(x),int(y)),10,(255, 20, 147),cv2.FILLED)
        img = cv2.addWeighted(img, 1, canvas, 0.6, 0)# this is the memorization 

    return img,canvas # we return canvas cus there where our drawing is 

#preparing the webcam:
def start_cam():
    cap=cv2.VideoCapture(0)
    canvas=None
    while True:
        did,frame=cap.read()# to read the frame 
        if not did: break
        #we modify our frame as we want aka calling the code main function :
        frame = cv2.flip(frame, 1)
        main_frame,canvas=functional(frame,canvas)# give it what to draw on 
        cv2.imshow("paint",main_frame)
        if cv2.waitKey(1) & 0xFF ==ord("q"):break
    cap.release()
    cv2.destroyAllWindows()

start_cam()
#C:\Users\gtx\miniconda3\envs\cv10\python.exe
















