import cv2
import cvzone

# importtin the model :
from cvzone.HandTrackingModule import HandDetector
#instantiation :
detector=HandDetector(maxHands=2,detectionCon=0.8,minTrackCon=0.5)

#the code main function:
def hand_detector(frame):
    #using the methodes of our module :
    hands,img=detector.findHands(frame,draw=True)
    return img 

#preparing the webcam:
def start_cam():
    cap=cv2.VideoCapture(0)
    while True:
        did,frame=cap.read()# to read the frame 
        if not did: break
        #we modify our frame as we want aka calling the code main function :
        hand_detected=hand_detector(frame)
        cv2.imshow("name",hand_detected)
        if cv2.waitKey(1) & 0xFF ==ord("q"):break
    cap.release()
    cv2.destroyAllWindows()

start_cam()


















