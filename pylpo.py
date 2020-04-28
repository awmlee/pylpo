# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:24:20 2020

@author: 
Alan Lee
@Warranty:
Absolutely none, expressed or implied.
"""

import pystray                              
from PIL import Image, ImageDraw, ImageFont
import time
import sys
import wmi
import pythoncom


oldcapacity=0
def getbatt(c,t):
    global oldcapacity
    capacity = 0
    temp=0
    discharge=0
    hoursleft=0
    #works on HP envy laptop:
    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    #Different brands might require this:
    #batts = t.ExecQuery('Select * from BatteryStatus ')
    
    for i, b in enumerate(batts):
        watts=b.DischargeRate/1000.0
        #print ('DischargeRate:     ' + str(b.DischargeRate)
        capacity+=b.RemainingCapacity
    #discharge=(oldcapacity-capacity)
    oldcapacity=capacity
    watthours=(capacity/1000.0)
    if discharge != 0:
        hoursleft=(capacity/discharge/1000)    
    batts1 = c.CIM_Battery(Caption = 'Portable Battery')
    return watts,watthours,hoursleft

def callback(icon):
    image = Image.new('RGB', (128,128), (255,255,255)) # create new image
    pythoncom.CoInitialize()
    c = wmi.WMI()
    t = wmi.WMI(moniker = "//./root/wmi")
    watts=0
    watthours=0
    hoursleft=0
    while True:
        watts,watthours,hoursleft = getbatt(c,t)
        img = image.copy()
        dc = ImageDraw.Draw(img)
        #dc.rectangle([0, 128, 128, 128-(percent * 128) / 100], fill='blue')
        txt="{0:.2f}\n{1:.2f}\n{2:.2f}"
        dc.text((10,0), txt.format(watts,watthours,hoursleft), font=font, fill=(0,0,0,255))
        icon.icon = img
        txtlong="Watts: {0:.3f}\nWatthours: {1:.3f}\nHours left: {2:.3f}"
        icon.title=txtlong.format(watts,watthours,hoursleft)
        time.sleep(3)

font = ImageFont.truetype(font="arial.ttf",size=40)
image = Image.new('RGB', (128,128), (255,255,255)) # create new image
icon = pystray.Icon(name ="PowerMon", title ="Power Monitor", menu =None,icon=image)
icon.visible = True
icon.run(setup=callback)    