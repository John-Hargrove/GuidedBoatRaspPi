import ServerHost #handles the server hosting
import MotorControllers
import GpsModule
import requests
import json

from flask import Flask, Response, Request
import cv2 #from opencv-python

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # 0 = first USB camera

def main():
    foo = 1

if __name__ == "__main__":
    main()
