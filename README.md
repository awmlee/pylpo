# PYLPO (Python Laptop Power)

## What:
  
Did you know that windows has more information on your laptop power consumption and battery state than windows typically reports?
  
Pylpo (Python Laptop Power) Creates a Windows systray icon that displays instantaneous power consumption (in watts) of a laptop running on battery.  It also shows battery charge (in watt*hours) and estimated battery life.  Pylpo digs through WMI  to get more power details than are typically available.  WMI access is made availble by the excellent python module wmi (see references).

## Why:
To maximize battery life on long trips, displaying the instantaneous power is a useful optimization tool.  You can immediatly see the effect of dimming your screen, and switching the cpu to low power mode.  You can also see more subtle effects like disabling software, the touchscreen, USB controllers, Network controllers or integrated GPU.  (For me, disabling the integrated GPU in windows actually increases the power consumption, because GPU chip doesn't actually power down).

You can also compare your results with notebookcheck.com's results for the same laptop.  


## Supported systems:

Windows only -- uses the windows WMI service to periodically poll battery and power stats from the system.  Works on HP envy laptop (2017).  May require tweaking with other windows laptops.  Tweaking is easy with the WMI explorer tool (see references below).
  
  
## Dependencies:

```
pystray: 	module for handling the display of the system tray icon  
PIL:		drawing module to produce the actual icon 
wmi:		windows management interface, python implementation.  
pythoncom:	used to interface wmi 
```  
  
## Install:
  
```
pip install pystray  
pip install wmi  		
pip install pythoncom  
```
  
run:
```
python pylpo.py
```
  
## References:
  
The WMI Module is really the key here. [WMI](https://pypi.org/project/WMI/)  
To figure out what resources you need from WMI I used [WMI Explorer](https://devblogs.microsoft.com/scripting/weekend-scripter-the-wmi-explorer-tool/)
  
## To Do:  
  
Remove pythoncom, it really shouldn't be necessary.

## Who:
  
Alan Lee [LongWave Photonics](https://longwavephotonics.com)
  

  
