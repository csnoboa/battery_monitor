import psutil
from win10toast import ToastNotifier
import time

while True:

    min_bat = 35
    max_bat = 75
    sleep_time = 60

    battery = psutil.sensors_battery()

    plugged = battery.power_plugged
    
    percent = battery.percent
        
    toaster = ToastNotifier()
        
    if percent <= min_bat and not plugged:
        toaster.show_toast("Plug the Battery Now!","The percent of the battery is: " + str(percent) + "% !!!")
        
    elif percent >= max_bat and plugged:
        toaster.show_toast("Unplug the Battery Now!","The percent of the battery is: " + str(percent) + "% !!!")
        
    time.sleep(sleep_time)
    
    
    

