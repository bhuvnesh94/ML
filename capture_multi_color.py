#!/usr/bin/python3
import cv2

# starting camera
cap=cv2.VideoCapture(0)

while True:
        status,frame=cap.read
