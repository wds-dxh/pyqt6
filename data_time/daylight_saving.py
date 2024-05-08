'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-07 19:16:30
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-07 19:16:33
FilePath: /pyqt6/data_time/daylight_saving.py
Description: pyqt6获取夏令时
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
# file: daylight_saving.py
#!/usr/bin/python

from PyQt6.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()

print(f'Time zone: {now.timeZoneAbbreviation()}')

if now.isDaylightTime():
    print('The current date falls into DST time')
else:
    print('The current date does not fall into DST time')