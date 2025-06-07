from SharedData import SharedData
shared_data = SharedData()

import serial
import adafruit_gps
import pigpio

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

# Start using the GPS
gps.send_command(b"PMTK220,200")  # Update every 200 milliseconds
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")  # NMEA sentences to output

import pigpio
import time

class PWMReader:
    def __init__(self, pi, gpio_pin):
        self.pi = pi
        self.gpio_pin = gpio_pin
        self.high_tick = None
        self.last_tick = None
        self.period = None
        self.high_time = None
        self.duty_cycle = 0
        self.frequency = 0

        # Set pin as input
        self.pi.set_mode(gpio_pin, pigpio.INPUT)
        self.cb = self.pi.callback(gpio_pin, pigpio.EITHER_EDGE, self._cbf)

    def _cbf(self, gpio, level, tick):
        if level == 1:  # Rising edge
            if self.last_tick is not None:
                self.period = pigpio.tickDiff(self.last_tick, tick)
                self.frequency = 1e6 / self.period if self.period > 0 else 0
                if self.high_time is not None:
                    self.duty_cycle = (self.high_time / self.period) * 100
            self.high_tick = tick
            self.last_tick = tick

        elif level == 0:  # Falling edge
            if self.high_tick is not None:
                self.high_time = pigpio.tickDiff(self.high_tick, tick)

    def get_pwm(self):
        return self.frequency, self.duty_cycle

    def cancel(self):
        self.cb.cancel()

def sensors_main():
    pi = pigpio.pi()
    if not pi.connected:
        print("Failed to connect to pigpio daemon.")
        exit(1)

    # Define the GPIO pins you want to monitor
    pwm_pins = [17, 27, 22, 23, 24]
    # GPIO Num: 17, 27, 22, 23, 24
    # Pin Num: 11, 13, 15, 16, 18

    readers = {}

    for pin in pwm_pins:
        readers[pin] = PWMReader(pi, pin)

    while True:
        gps.update()
        if gps.has_fix:
            shared_data.gps_data = {
                "lat": gps.latitude,
                "lon": gps.longitude,
                "alt": gps.altitude_m,
                "time": gps.timestamp_utc,
            }

        shared_data.pwm_data = {
            pin: reader.get_pwm() for pin, reader in readers.items()
        }

