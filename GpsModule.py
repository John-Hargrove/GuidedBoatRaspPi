from Main import *
import time

# Use UART / serial connection
uart = busio.UART("/dev/serial0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

# Start using the GPS
gps.send_command(b"PMTK220,1000")  # Update every 1 second
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")  # NMEA sentences to output

last_print = time.monotonic()

while True:
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            print("Waiting for fix...")
            continue

        print("=" * 40)
        print("Fix timestamp: {}".format(gps.timestamp_utc))
        print("Latitude: {:.6f} degrees".format(gps.latitude))
        print("Longitude: {:.6f} degrees".format(gps.longitude))
        print("Fix quality: {}".format(gps.fix_quality))
        print("Satellites: {}".format(gps.satellites))