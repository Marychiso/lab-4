# Stores a simple recommendation from the doctor to the patient.

class Recommendation:
    def __init__(self, doctor_name, patient_name, text):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.text = text
