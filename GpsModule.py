from Main import *

def start_gps_module():
    # Use UART / serial connection
    uart = busio.UART("/dev/serial0", baudrate=9600, timeout=10)
    gps = adafruit_gps.GPS(uart, debug=False)

    # Start using the GPS
    gps.send_command(b"PMTK220,1000")  # Update every 1 second
    gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")  # NMEA sentences to output