import numpy as np
import mediapipe as mp
import time
from turtle import *
from cProfile import label
import tkinter as tk
from tkinter import ttk
# import microcontrollerardino as micro
from tkinter import *
import cv2
from PIL import Image, ImageTk

windowbar=Tk()
windowbar.title("RC Car control using Hand Gestures")
windowbar.configure(bg="red")
titlefirst = Label(windowbar, text="Gestured control RC car", font=("Calibri",30), bg="pink", 
        fg="white", relief=GROOVE).place(relx=0.5,rely=0.1, anchor="center")

f1 = tk.LabelFrame(windowbar, bg="red")
f1.place(relx=0.5, rely=0.5, anchor="center")
L1 = tk.Label(f1, height=500, width=660, bg="white")
L1.pack()

Label(windowbar,text="Tehzeeb imtiaz 2021_MC_73" ,font=("Calibri",25),bg='red').place(relx=0.0,rely=0.4)  
Label(windowbar,text="Amina Ahmed 2021_MC_71" ,font=("Calibri",25),bg='red').place(relx=0.0,rely=0.5)

v=StringVar()
str(v.get()) 

livevar=IntVar() 
livevar.set(0)

mpDraw = mp.solutions.drawing_utils
mpHand = mp.solutions.hands
hands = mpHand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, 
                     static_image_mode=False, max_num_hands=1
                     )

global direction
direction = 'Up'

def videoClick(Adressofvideo):
    livevar.set(1)

def closewindow():
    windowbar.destroy()

Button(f1, text="Exit window", bg='white', fg='black', font=("Calibri", 20, "bold"), command=closewindow).place(relx=0.100, rely=0.100, anchor="center")

cap = cv2.VideoCapture(0)
handtips_top=[4,8,12,16,20]
def update_frame():
    while True:
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)
            lmList=[]
            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    myHands=results.multi_hand_landmarks[0]
                    for id, lm in enumerate(myHands.landmark):
                        h,w,c=frame.shape
                        cx,cy= int(lm.x*w), int(lm.y*h)
                        lmList.append([id,cx,cy])
                    mpDraw.draw_landmarks(frame, hand_landmark, mpHand.HAND_CONNECTIONS)
            fingers=[]
            if len(lmList)!=0:
                if lmList[handtips_top[0]][1] > lmList[handtips_top[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1,5):
                    if lmList[handtips_top[id]][2] < lmList[handtips_top[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total=fingers.count(1)

                # direction = micro.RCCAR(total)

                if total==0:
                
                    cv2.putText(frame, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 8)
                    print("brake")
                

                if total==5:

                    cv2.putText(frame, " FORWARD", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 8)
                    print("forward")            
                if total==2:

                    cv2.putText(frame, " RIGHT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    print("right")


                if total==3:
                    #cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, " LEFT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    print("left")

                if total==4:
                    #cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, "REVERSE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
                    print("REVERSE") 
                # cv2.imshow("Frame",frame)
                k=cv2.waitKey(1)

        imgtk = ImageTk.PhotoImage(Image.fromarray(frame))
    
        L1["image"] = imgtk
        windowbar.update()
    
  

update_frame()

windowbar.mainloop()

