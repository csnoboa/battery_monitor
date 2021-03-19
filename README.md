# battery_monitor
An application made in Python to show the user when to plug in or unplug the charger from his notebook, in order to increase battery life.


0: Install python 3.7: https://www.python.org/ftp/python/3.7.7/python-3.7.7.exe

1: Install python dependencies: pip install -r requirements.txt

1: Put the "battery_monitor.py" in somewhere you will not delete ( Ex: C:\scr\python\battery_monitor.py )
       
       If you put in other directory, change the path in the battery_monitor.bat

2: Alter the config.json for the numbers you would like:
  "min_battery" : below this percentage you will be notified to place the notebook to charge,
  "max_battery" : above this percentage, you will be notified to remove the charger from the notebook,
  "time_check" : time interval (in seconds) that the program will check the battery percentage

3: Now, put the files "battery_monitor.bat" and "config.json" in the folder: 

       %appdata%\Microsoft\Windows\Start Menu\Programs\Startup\
