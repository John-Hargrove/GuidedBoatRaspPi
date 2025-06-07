#https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/ raspberry pi pinout

#WIRING ----------------------------

#GPS MODULE ------------------
# GPS Pin --> Raspberry Pi Pin
# VIN --> 4 (5V)
# GND --> 6 (GND)
# TX --> 10 (GPIO15, RXD)
# RX --> 8 (GPIO14, TXD)

import threading
import time

import Sensors

#data_thread = threading.Thread(target=Sensors.sensors_main)



def main():
    #data_thread.start()

    Sensors.sensors_main()

    # while True:
    #     print(time.time())

if __name__ == "__main__":
    main()


