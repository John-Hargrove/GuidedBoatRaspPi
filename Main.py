import ServerHost #handles the server hosting
import MotorControllers
import GpsModule
import requests
import json

import adafruit_gps
import board
import time
import busio

from flask import Flask, Response, Request
import cv2 #from opencv-python

#https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/ raspberry pi pinout
# GPS Pin --> Raspberry Pi Pin
# VIN --> 4 (5V)
# GND --> 6 (GND)
# TX --> 10 (GPIO15, RXD)
# RX --> 8 (GPIO14, TXD)
app = Flask(__name__)
camera = cv2.VideoCapture(0)  # 0 = first USB camera

def main():
    foo = 0

if __name__ == "__main__":
    main()
