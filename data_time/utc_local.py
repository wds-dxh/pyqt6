'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-07 19:08:45
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-07 19:11:35
FilePath: /pyqt6/data_time/utc_local.py
Description: pyqt6获取标准时间和本地时间
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
# file: utc_local.py
#!/usr/bin/python
#UTC时间是世界协调时间，也称为格林尼治标准时间（GMT）。
from PyQt6.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print('Local datetime: ', now.toString(Qt.DateFormat.ISODate))
print('Universal datetime: ', now.toUTC().toString(Qt.DateFormat.ISODate))

print(f'The offset from UTC is: {now.offsetFromUtc()} seconds')


print('Local datetime: ', now.toString(Qt.DateFormat.ISODate))

#总结
"""
1. QDateTime类的toUTC()方法将本地时间转换为UTC时间。
2. QDateTime类的offsetFromUtc()方法返回本地时间与UTC时间之间的偏移量（以秒为单位）。
"""