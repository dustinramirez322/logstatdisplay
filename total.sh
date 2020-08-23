#!/bin/bash
cat /log/$(date +\%Y-%m-%d)-syslog.log | egrep /[2][2-3]$ | awk '{print $12}' | wc -l
