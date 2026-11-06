import cv2
import mediapipe as mp
import time 

cap= cv2.VideoCapture(0)

faceDetect= mp.solutions.face_detection
mpDraw= mp.solutions.drawing_utils
faceDetection= faceDetect.FaceDetection()
ctime,ptime=0,0
while True:
    success,img=cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res=faceDetection.process(imgRGB)
    if res.detections:
        for id , detect in enumerate(res.detections):
            mpDraw.draw_detection(img, detect)
            print(id, detect.score)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,"fps:"+str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("img",img)
    cv2.waitKey(1)