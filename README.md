# logstatdisplay
This is a small collection of bash scripts I use to display, interact with, and maintain network information I pull from syslog.

These scripts are ran on a raspberry pi that also serves as a syslog server.  The scripts parse the days file and update a display in realtime.

My syslog is configured to create logs that follow at YYYY-MM-DD-syslog.log format.  As such the scripts reference the log file in this manner.  If your logs are created in a different format either:

1.  Adjust this script to match the correct log file name.
2.  Adjust your rsyslog (or other syslog option) to create names in this format.

Place .sh files in appropriate location that is included in $PATH variable.  Otherwise specifiy entire directory path of the file.

CRON 'Log Moves.py' to run on the first of every month for automatic log moves.

uctronics.py can be ran from any location.

ePaper.py is only able to be ran in directory created by manufacturer at this time.  Working on updating script to place it in $PATH location.

-----------------------------------------------------------------------------------------
I have used the bash scripts with both an e-Paper display and UCTRONICS .96 inch display.

Link to UCTRONICS:

https://www.amazon.com/UCTRONICS-SSD1306-Self-Luminous-Display-Raspberry/dp/B072Q2X2LL/

Link to e-Paper:

https://www.amazon.com/gp/product/B07P6MJPTD/
