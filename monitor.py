# The monitor system receives alerts from devices.
# It checks if they are critical and forwards them to a doctor.

class MonitorSystem:
    def __init__(self, doctor):
        self.doctor = doctor
        self.alerts = []

    def process_alert(self, alert):
        # Save each alert to the system
        self.alerts.append(alert)

        # Send to doctor for review
        recommendation = self.doctor.review_alert(alert)

        # Add recommendation to the patient
        alert.patient.recommendations.append(recommendation)
