import threading

class SharedData:
    def __init__(self):
        self.lock = threading.Lock()
        self.gps_data = None
        self.pwm_data = {}