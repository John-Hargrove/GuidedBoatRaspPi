import ServerHost
import MotorControllers
import GpsModule

from flask import Flask, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # 0 = first USB camera

def main():
    foo = 1

if __name__ == "__main__":
    main()
