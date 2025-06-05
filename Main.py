#https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/ raspberry pi pinout
# GPS Pin --> Raspberry Pi Pin
# VIN --> 4 (5V)
# GND --> 6 (GND)
# TX --> 10 (GPIO15, RXD)
# RX --> 8 (GPIO14, TXD)
import requests
import json
import busio
import serial

import adafruit_gps #from adafruit-pythoncircuit-gps
import time


import ServerHost #handles the server hosting
import MotorControllers #handles the motor controllers
import GpsModule #handles the GPS module



from flask import Flask, Response, Request
import cv2 #from opencv-python

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # 0 = first USB camera

def main():
    foo = 0

if __name__ == "__main__":
    main()
