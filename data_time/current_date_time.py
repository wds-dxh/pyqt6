'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-07 19:00:04
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-07 19:12:08
FilePath: /pyqt6/data_time/current_date_time.py
Description: 学习PyQt6-QDate、QTime、QDateTime
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: current_date_time.py

from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.DateFormat.ISODate))  #ISODate表示国际标准日期格式
print(now.toString(Qt.DateFormat.RFC2822Date))  #RFC2822Date表示RFC2822日期格式

datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()
print(time.toString(Qt.DateFormat.ISODate))

#总结
"""
1. QDate、QTime、QDateTime类提供了日期、时间和日期时间的功能。
2.都有currentDate()、currentTime()、currentDateTime()静态方法，返回当前日期、时间和日期时间。
3.可以使用toString()方法将日期、时间和日期时间转换为字符串。（可以使用Qt.DateFormat枚举值指定格式）
--Qt.DateFormat枚举值：ISODate：国际标准日期格式；RFC2822Date：RFC2822日期格----中国是ISODate
"""