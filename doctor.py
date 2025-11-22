class Doctor:
    def __init__(self, name):
        self.name = name
# The doctor reviews alerts sent from the monitor system
# and gives simple recommendations based on the alert.

    def review_alert(self, alert):
        from recommendation import Recommendation

        # Very simple rule for recommendation
        if alert.urgent:
            text = "Your reading is high. Please visit the hospital."
        else:
            text = "Your reading is slightly off. Keep monitoring it."

        return Recommendation(self.name, alert.patient.name, text)
