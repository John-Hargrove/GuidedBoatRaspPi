#https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/ raspberry pi pinout

# WIRING ----------------------------

# GPS MODULE ------------------
# GPS Pin --> Raspberry Pi Pin
# VIN --> 4 (5V)
# GND --> 6 (GND)
# TX --> 10 (GPIO15, RXD)
# RX --> 8 (GPIO14, TXD)

# RECEIVER ------------------
# Receiver Pin --> Raspberry Pi Pin
# Channel # --> 11 (GPIO17)
# Channel # --> 13 (GPIO27)
# Channel # --> 15 (GPIO22)
# Channel # --> 16 (GPIO23)
# Channel # --> 18 (GPIO24)


import threading
import time

import Sensors

data_thread = threading.Thread(target=Sensors.sensors_main, daemon=True)


def main():
    data_thread.start()
    while True:
        print(time.time())

if __name__ == "__main__":
    main()


