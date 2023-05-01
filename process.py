from keras.preprocessing.image import img_to_array,load_img
import numpy as np
import glob
import os 
import cv2
from keras.layers import Conv3D,ConvLSTM2D,Conv3DTranspose
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint, EarlyStopping
import imutils
from skimage.transform import resize
import argparse

imagestore = []
def store(image_path):
	img = load_img(image_path)
	img = img_to_array(img)
	#Resize the Image to (227,227,3) for the network to be able to process it.
	img = resize(img,(227,227,3))
	#Convert the Image to Grayscale
	gray = 0.2989*img[:,:,0]+0.5870*img[:,:,1]+0.1140*img[:,:,2]
	imagestore.append(gray)




framepath = "E:/semester 5/Project1/UCSD_Anomaly_Dataset.v1p2/UCSDped2/Train"
fps = 30
for i in os.listdir(framepath):
    for images in os.listdir(framepath+i):
          store(framepath + i +'/'+images)