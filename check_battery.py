import psutil
import time
from Speak_Mark import speak
import random
from Random_sentences import *

def battery_alert():
    time.sleep(15)
    while True:
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent <= 30:
            lowBattery=random.choice(batteryDLG)
            speak(lowBattery)
        elif percent <= 10:
            lastBattery=random.choice(lastChanceDLG)
            speak(lastBattery)
        elif percent <= 50:
            Battery50=random.choice(batteryLowDLG)
            speak(Battery50)
        elif percent == 100:
            BatteryFull=random.choice(batteryFullDLG)
            speak(BatteryFull)
        else:
            pass
        
        time.sleep(1500)  # Wait for 25 minutes before checking again

def battery_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    speak(f"The device is running on {percent}% battery power.")

def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                BatteryPlug=random.choice(chargingDLG)
                speak(BatteryPlug)
            else:
                BatteryPower=random.choice(batteryPowerDLG)
                speak(BatteryPower)
            
            previous_state = battery.power_plugged
        
        # time.sleep(1) 

# battery_alert()
# battery_percentage()
# check_plugin_status()