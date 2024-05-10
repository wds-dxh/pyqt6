'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-10 14:59:14
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-10 15:07:16
FilePath: /pyqt6/Events_signals/custom_signal.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: custom_signal.py

import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):

    closeApp = pyqtSignal() #创建一个信号


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close) #将信号连接到QMainWindow的close()方法，收到信号就会关闭窗口

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Emit signal')
        self.show()


    def mousePressEvent(self, e):

        self.c.closeApp.emit()  #发射信号,emit()方法发射信号


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()