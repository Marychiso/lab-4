class Alert:
    def __init__(self, patient, vital_name, value, critical):
        self.patient = patient
        self.vital_name = vital_name
        self.value = value
        self.critical = critical
        self.message = f"{vital_name} is {value}"
# This class stores basic information about an alert.
# It includes the patient, the vital sign name, the value, and whether it is critical.