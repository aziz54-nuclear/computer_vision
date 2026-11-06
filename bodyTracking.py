import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpDraw=mp.solutions.drawing_utils
pose=mp.solutions.pose
pose=pose.Pose()

while True:
    success, img = cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=pose.process(imgRGB)
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        for id , lm in enumerate(result.pose_landmarks.landmark):
            pass
    cv2.imshow("image",img)
    cv2.waitKey(1)