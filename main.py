# It creates a patient, doctor, device, and monitor system.
# The device sends readings and the doctor responds with recommendations.

from patient import Patient
from doctor import Doctor
from wearable import WearableDevice
from monitor import MonitorSystem

# This file simulates how the objects in the system interact.
def main():
    # Create doctor and monitor
    doctor = Doctor("Dr. Mary")
    monitor = MonitorSystem(doctor)

    # Create patient and connect device
    patient = Patient("Willaim")
    device = WearableDevice("W1")
    patient.add_device(device)

    # Vitals the device will send
    vitals = ["heart rate", "blood pressure", "oxygen level"]

    print("--- Sending Readings ---")
    for v in vitals:
        device.send_to_monitor(monitor, v)

    # Display all alerts
    print("\n--- Alerts Generated ---")
    for a in monitor.alerts:
        print(a.message)

    # Display recommendations
    print("\n--- Recommendations for Patient ---")
    for r in patient.recommendations:
        print(r.text)


main()


# Reflection:
# Creating this Remote Health Monitoring System helped me understand how different classes interact in an object-oriented program. 
#The easy part was writing the basic classes such as Patient, Doctor, 
#and Alert because they only store simple information. 
#Connecting the classes together was a bit harder than i thought it would be , 
#especially figuring out the part  where the wearable device sends a reading to the monitor, 
#then the monitor creates an alert and sends it to the doctor. 
#Another thing that was a bit difficult was deciding where certain actions should happen, 
#like where the doctor or the monitor should create the recommendation and i also encountered so many errors 
#and it even got frustrating at some point and i dont know if everything is going to run simultaneously but i tried by best . 
#In the end I kept everything simple so the code is easier to read . 



