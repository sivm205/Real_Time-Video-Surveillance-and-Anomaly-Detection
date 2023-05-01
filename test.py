import cv2
import numpy as np 
from keras.models import load_model
import argparse
from PIL import Image
from datetime import datetime
import imutils

def test_Detection_camera():
        
    text = str(datetime.now())
    def mean_squared_loss(x1,x2):
        difference=x1-x2
        a,b,c,d,e=difference.shape
        n_samples=a*b*c*d*e
        sq_difference=difference**2
        Sum=sq_difference.sum()
        distance=np.sqrt(Sum)
        mean_distance=distance/n_samples

        return mean_distance


    model=load_model("model.h5")
    #vid_path = "E:/Telegram/Tg @StreamersHub Loki S01E03 Dual 1080p 10bit HEVC"
    #vid_path = "D:/Programs/Anomaly Detection/Data Videos/real life violence situations/Real Life Violence Dataset/NonViolence/NV_87.mp4"
    #vid_path = "D:/Programs/Anomaly Detection/Data Videos/real life violence situations/Real Life Violence Dataset/Violence/V_17.mp4"

    cap = cv2.VideoCapture(0)
    if(cap):
        print("Video found successfully\n")
    else:
        print("Not able to locate video from the specified path\n")

    while cap.isOpened():
        imagedump=[]
        ret,frame=cap.read()

        for i in range(10):
            ret,frame=cap.read()
            if not ret:
                break
            image = imutils.resize(frame,width=700,height=600)

            frame = cv2.resize(frame, (227,227), interpolation = cv2.INTER_AREA)
            gray = 0.2989*frame[:,:,0]+0.5870*frame[:,:,1]+0.1140*frame[:,:,2]
            gray = (gray-gray.mean())/gray.std()
            gray = np.clip(gray,0,1)
            imagedump.append(gray)

        imagedump = np.array(imagedump)

        imagedump.resize(227,227,10)
        imagedump = np.expand_dims(imagedump,axis=0)
        imagedump = np.expand_dims(imagedump,axis=4)

        output = model.predict(imagedump)

        loss = mean_squared_loss(imagedump,output)

        if frame.any()==None:
            print("none")

        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
        if loss>0.00068:
            print('Abnormal Event Detected')
            cv2.rectangle(frame,(900,450),(500,200),(0,255,0),6)
            cv2.putText(image,"Alert!!! Anomalous Behaviour Detected",(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
            cv2.putText(image, text, (30,40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
        else:
            print("Bunch is normal")
            cv2.rectangle(frame,(900,450),(500,200),(0,255,0),6)
            cv2.putText(image,"Normal!!!! ",(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
            cv2.putText(image, text, (30,40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

        cv2.imshow("video",image)

    cap.release()
    cv2.destroyAllWindows()

def test_Detection(video_path):
        
    text = str(datetime.now())
    def mean_squared_loss(x1,x2):
        difference=x1-x2
        a,b,c,d,e=difference.shape
        n_samples=a*b*c*d*e
        sq_difference=difference**2
        Sum=sq_difference.sum()
        distance=np.sqrt(Sum)
        mean_distance=distance/n_samples

        return mean_distance


    model=load_model("model.h5")
    #vid_path = "E:/Telegram/Tg @StreamersHub Loki S01E03 Dual 1080p 10bit HEVC"
    #vid_path = "D:/Programs/Anomaly Detection/Data Videos/real life violence situations/Real Life Violence Dataset/NonViolence/NV_87.mp4"
    #vid_path = "D:/Programs/Anomaly Detection/Data Videos/real life violence situations/Real Life Violence Dataset/Violence/V_17.mp4"
    vid_path = video_path
    cap = cv2.VideoCapture(vid_path)
    if(cap):
        print("Video found successfully\n")
    else:
        print("Not able to locate video from the specified path\n")

    while cap.isOpened():
        imagedump=[]
        ret,frame=cap.read()

        for i in range(10):
            ret,frame=cap.read()
            if not ret:
                break
            image = imutils.resize(frame,width=700,height=600)

            frame = cv2.resize(frame, (227,227), interpolation = cv2.INTER_AREA)
            gray = 0.2989*frame[:,:,0]+0.5870*frame[:,:,1]+0.1140*frame[:,:,2]
            gray = (gray-gray.mean())/gray.std()
            gray = np.clip(gray,0,1)
            imagedump.append(gray)

        imagedump = np.array(imagedump)

        imagedump.resize(227,227,10)
        imagedump = np.expand_dims(imagedump,axis=0)
        imagedump = np.expand_dims(imagedump,axis=4)

        output = model.predict(imagedump)

        loss = mean_squared_loss(imagedump,output)

        if frame.any()==None:
            print("none")

        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
        if loss>0.00068:
            print('Abnormal Event Detected')
            cv2.rectangle(frame,(900,450),(500,200),(0,255,0),6)
            cv2.putText(image,"Alert!!! Anomalous Behaviour Detected",(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
            cv2.putText(image, text, (30,40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
        else:
            print("Bunch is normal")
            cv2.rectangle(frame,(900,450),(500,200),(0,255,0),6)
            cv2.putText(image,"Normal!!!! ",(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
            cv2.putText(image, text, (30,40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

        cv2.imshow("video",image)

    cap.release()
    cv2.destroyAllWindows()

