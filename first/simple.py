'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-07 19:29:31
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-08 12:50:12
FilePath: \pyqt6\first\simple.py
Description: pyqt6的第一个例子
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: simple.py

"""
ZetCode PyQt6 tutorial

In this example, we create a simple
window in PyQt6.

Author: Jan Bodnar
Website: zetcode.com
"""


import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

def main():

    app = QApplication(sys.argv)

    w = QWidget() # 创建一个窗口
    w.resize(250, 200)
    w.move(100, 300)

    label = QLabel(w) # 创建一个标签
    label.setText('Hello World!')
    label.move(110, 85)
    label.setStyleSheet('color: red; font-size: 20px; font-weight: bold;')
    label.show() 

    w.setWindowTitle('title')
    w.show()

    sys.exit(app.exec())        #使用sys.exit()方法确保程序完全退出，不会出现崩溃的情况，
                                    #app.exec()方法会进入主循环主循环用于接收件，当调用exit()方法或主窗口被销毁时，主循环会事，退出。


if __name__ == '__main__':
    main()