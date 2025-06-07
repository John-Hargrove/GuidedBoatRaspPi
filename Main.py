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

#new
import threading
import time

from SharedData import SharedData
import Sensors

shared_data = SharedData()
data_thread = threading.Thread(target=Sensors.sensors_main, args=(shared_data,), daemon=True)


def main():
    data_thread.start()
    while True:
        with shared_data.lock:
            print("--- MAIN LOOP ---")
            if shared_data.gps_data:
                print(f"GPS: {shared_data.gps_data}")
            for pin, (freq, duty) in shared_data.pwm_data.items():
                print(f"GPIO {pin}: {freq:.1f} Hz, {duty:.1f}% duty")
        time.sleep(1)

if __name__ == "__main__":
    main()


