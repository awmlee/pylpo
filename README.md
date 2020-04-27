What:
Pylpo (Python Laptop Power) Creates a systray icon that displays instantaneous power consumption (in watts) of a laptop running on battery.  Also shows battery charge (in watt*hours) and estimated battery life.

Why:
To maximize battery life on long trips, displaying the instantaneous power is useful.  You can immediatly see the effect of dimming your screen, and switching the cpu to low power mode.  You can also see more subtle effects like disabling software, the touchscreen, USB controllers, Network controllers or integrated GPU.  (Disabling the integrated GPU actually increases the power consumption, because GPU doesn't actually power down).

You can also compare your results with notebookcheck.com's results for the same laptop.  


Supported systems:

Windows only -- uses the windows WMI service to periodically poll battery and power stats from the system.  Works on my HP envy laptop (2017).


Dependencies:

pystray: 	for the system tray icon
PIL:		for the icon
wmi:		windows management interface, python implementation.  
pythoncom:	used to interface wmi 

Install:

pip install systray
pip install wmi
pip install pythoncom


python pilpo

To Do:
Remove pythoncom