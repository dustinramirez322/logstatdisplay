#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
if os.path.exists(libdir):
    sys.path.append(libdir)
import subprocess
from waveshare_epd import epd2in9
from PIL import Image,ImageDraw,ImageFont
import traceback
import time
while (True):
    
    epd = epd2in9.EPD()
    epd.init(epd.lut_full_update)
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    cmd = "total.sh"
    TOTS = subprocess.check_output(cmd, shell = True )
    cmd = "scan.sh"
    SCAN = subprocess.check_output(cmd, shell = True )
    cmd = "last.sh"
    LAST = subprocess.check_output(cmd, shell = True )

    draw.text((10, 0), 'Telnet and SSH Scans', font = font24, fill = 0)
    draw.text((10, 20), 'Total: ' +  str(TOTS, 'utf-8'), font = font24, fill = 0)
    draw.text((10, 40), 'Unique: ' + str(SCAN, 'utf-8'), font = font24, fill = 0)
    draw.text((10, 60), 'Last IP: ' + str(LAST, 'utf-8'), font = font24, fill = 0)
    time.sleep(5)
    epd.display(epd.getbuffer(Himage))

