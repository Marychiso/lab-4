# The wearable device takes random readings and sends them to the monitor system.
import random
from alert import Alert

class WearableDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.owner = None

    def take_reading(self, vital_name):
   # Generate a random value to imitate a real device
        value = random.randint(50, 200)
        critical = value > 130 or value < 40
        return Alert(self.owner, vital_name, value, critical)

    def send_to_monitor(self, monitor, vital_name):
        # Send the reading to the monitor system
        reading = self.take_reading(vital_name)
        monitor.process_alert(reading)
