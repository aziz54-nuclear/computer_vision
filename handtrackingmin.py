import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands(
    static_image_mode=False,
    max_num_hands=4,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
ptime=0
ctime=0
while True:
    success, img=cap.read()
    h,w,c=img.shape
    #drawing a rectangle on the frame
    rect_w, rect_h = 200, 150    # rectangle size in pixels
    x1 = w // 2 - rect_w // 2    # top-left corner
    y1 = h // 2 - rect_h // 2
    x2 = x1 + rect_w             # bottom-right corner
    y2 = y1 + rect_h

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLM in results.multi_hand_landmarks:
            for id,lm in enumerate(handLM.landmark):
                
                cx,cy=int(lm.x*w),int(lm.y*h)
                if( id==4 or id==8 or id==12 or id==16 or id==20):
                    
                    if(x1<cx<x2 and y1<cy<y2):
                        cv2.putText(img,"Fingers in the rectangle",(10,150),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
                        cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)
                    #cv2.circle(img,(cx+10,cy+10),15,(255,0,255),cv2.FILLED)
            mp.solutions.drawing_utils.draw_landmarks(img, handLM, mpHands.HAND_CONNECTIONS)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)