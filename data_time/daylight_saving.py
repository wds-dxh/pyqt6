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

"""
总结--DST是夏令时的缩写，是一种节约能源的方式，通过在夏季调整时钟来节约能源。
这个例子展示了如何使用PyQt6获取夏令时信息。
1.我们使用QDateTime.currentDateTime()方法获取当前日期和时间。
2.我们使用QDateTime.isDaylightTime()方法检查当前日期是否在夏令时。
3.timeZoneAbbreviation()方法返回当前时区的缩写。

"""