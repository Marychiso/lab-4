# This class represents a patient in the system.

class Patient:
    def __init__(self, name):
        self.name = name
        self.device = None
        self.recommendations = []

    def add_device(self, device):
        # Connect the device to the patient
        self.device = device
        device.owner = self
