#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:50:34 2020
Used to move logs into the appropriate folder.
On the 1st of each Month a folder will be created for the Month.
All logs from the previous Month will be moved to the appropriate folder.
On the 1st Day of the year a folder will be created for the Year.
All folders from the previous year will be moved to the appropriate folder.
@author: dustin
"""

import os
import time
import datetime
import shutil

#Define today, first day of the month, and lastMonth
#Used when migrating logs to a folder with last Month's name
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
lastYear = today - datetime.timedelta(days=365)

#Change to logs directory and list files in logs directory
os.chdir('/logs/')
fileNames = os.listdir('/logs/')


#If it is the first of the year make a directory
if time.strftime('%b%d') == 'Jan01':
    os.mkdir(lastYear.strftime('%Y') + '-Year-Logs')
    for f in fileNames:
        if(f.endswith('-Logs')):
            shutil.move(f, '/logs/' + lastYear.strftime('%Y') + '-Year-Logs')
            

#If it is the first of the month make a directory and move previous months logs
if time.strftime('%d') == str(1):
    os.mkdir('/logs/' + time.strftime('%b') + '-Logs')
    for f in fileNames:
        if(f.startswith(lastMonth.strftime('%Y-%m'))):
            shutil.move(f, '/logs/' + lastMonth.strftime('%b') + '-Logs')
       