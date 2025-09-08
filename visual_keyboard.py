import cv2
import cvzone
import numpy as np 
import time 

# importtin the model :
from cvzone.HandTrackingModule import HandDetector
#instantiation :
detector = HandDetector(detectionCon=0.5, maxHands=1,minTrackCon=0.5)
text=""
last_pressed= 0
#the code main function:
def index_detection(frame):
    hands, img = detector.findHands(frame, draw=True)#hands[0]["lmList"] has the 21 list of coordinates 
    h, w, _ = img.shape
    if hands:
        hand = hands[0]  # Get the first hand
        landmarks = hand["lmList"]  # List of 21 landmark points
        #each landmark store three vars [x, y,id]
        index_tip = landmarks[8]
        x,y,_=index_tip
        return img ,int(x),int(y)
    else:
        return img,None,None


#drawing the buttons :
def btn_draw(frame,index_x,index_y):
    global text
    global last_pressed
    keys = [
    ['Q','W','E','R','T','Y','U','I','O','P'],
    ['A','S','D','F','G','H','J','K','L'],
    ['Z','X','C','V','B','N','M']]
    h,w,_=frame.shape
    key_board_height=0.4*h
    #start=h-key_board_height
    start=0
    for i,row in enumerate(keys):
        num_keys=len(row)
        rec_width=w // num_keys
        rec_height = key_board_height // len(keys)
        for j, key in enumerate(row):
            x1 = j * rec_width
            y1 = start + i * rec_height
            x2 = x1 + rec_width
            y2 = y1 + rec_height
            # draw rectangle
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (160,32,141),-1)
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 0), 2)
            # draw letter
            cv2.putText(frame, key, (int(x1 + 10), int(y1 + rec_height - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            #_,index_x,index_y=index_detection(frame)
            if index_x is not None and index_y is not None :
                if x1 < index_x < x2 and  y1 < index_y < y2:
                    if time.time()-last_pressed > 2:
                     cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (251,198,207),-1)
                     text+=key
                     last_pressed=time.time()
    return frame

def displaying(frame):
    h,w,_=frame.shape
    display_height = int(0.1 * h)
    x3, y3 = 10, h - display_height - 10 
    x4, y4 = w - 10, h - 10
    # where tp print 
    cv2.rectangle(frame, (x3, y3), (x4, y4), (255, 255, 255), -1)
    cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 0), 3)
    cv2.putText(frame, text, (x3 + 10, y4 - 10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    return frame



#preparing the webcam:
def start_cam():
    cap=cv2.VideoCapture(0)
    canvas=None
    while True:
        did,frame=cap.read()# to read the frame 
        if not did: break
        #we modify our frame as we want aka calling the code main function :
        frame = cv2.flip(frame, 1)
        main_frame, index_x, index_y = index_detection(frame) 
        keybord = btn_draw(main_frame,index_x,index_y)  
        display = displaying(keybord)
        cv2.imshow("keyboard",display)
        if cv2.waitKey(1) & 0xFF ==ord("q"):break
    cap.release()
    cv2.destroyAllWindows()

start_cam()
#C:\Users\gtx\miniconda3\envs\cv10\python.exe visual_keyboard.py

