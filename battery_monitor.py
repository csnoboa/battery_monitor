import psutil
from win10toast import ToastNotifier
import time
import json

def run(configuration):
    while True:
        min_bat = configuration["min_battery"]
        max_bat = configuration["max_battery"]
        sleep_time = configuration["time_check"]

        battery = psutil.sensors_battery()

        plugged = battery.power_plugged
        
        percent = battery.percent
            
        toaster = ToastNotifier()
            
        if percent <= min_bat and not plugged:
            toaster.show_toast("Plug the Battery Now!","The percent of the battery is: " + str(percent) + "% !!!")
            
        elif percent >= max_bat and plugged:
            toaster.show_toast("Unplug the Battery Now!","The percent of the battery is: " + str(percent) + "% !!!")
            
        time.sleep(sleep_time)
        

def load_config():
    data = json.load(open('config.json'))
    return data
        

if __name__ == '__main__':
    configuration = load_config()
    print(configuration)
    run(configuration)
    

