# battery_monitor
An application made in Python to show the user when to plug in or unplug the charger from his notebook, in order to increase battery life.


# 0- Install Python.
Install python 3.7: https://www.python.org/ftp/python/3.7.7/python-3.7.7.exe

# 1- Install Project Dependencies.
Install project dependencies:
       pip install -r requirements.txt

# 2- Move the files to some folder you'll not delete. 
Put the "battery_monitor.py", "battery_monitor.bat" and "config.json" in somewhere you will not delete ( Ex: C:\scr\python\battery_monitor )
       
       If you put in other directory, change the path in the battery_monitor.bat

# 3- Configure the parameters (Optional)
Alter the config.json for the numbers you would like:
  "min_battery" : below this percentage you will be notified to place the notebook to charge,
  "max_battery" : above this percentage, you will be notified to remove the charger from the notebook,
  "time_check" : time interval (in seconds) that the program will check the battery percentage

# 4- Create a shortcut
Create a Shortcut of the "battery_monitor.bat": 

Right-click on the "battery_monitor.bat" file, and select "Create Shortcut"
[]

# 5- Put it to run every time you turn on the computer

For do this, you need to put the Shortcut in the folder:

       %appdata%\Microsoft\Windows\Start Menu\Programs\Startup\

# 6- Configure to run hidden (Optional)

Open the Properties from the Shortcut:
[]

Go to "General" and check the checkbox "Hidden":
[]