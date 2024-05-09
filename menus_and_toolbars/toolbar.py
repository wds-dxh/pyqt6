'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-09 15:09:05
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 15:11:17
FilePath: /pyqt6/menus_and_toolbars/toolbar.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: toolbar.py


import sys
from PyQt6.QtWidgets import QMainWindow,  QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), 'Exit', self)  #创建一个QAction对象
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(QApplication.instance().quit)

        self.toolbar = self.addToolBar('Exit')  #创建一个工具栏
        self.toolbar.addAction(exitAct)         #工具栏添加一个QAction对象

        self.setGeometry(300, 300, 640, 480)    #设置窗口的位置和大小，前两个参数是窗口的x和y坐标，后两个参数是窗口的宽度和高度
        self.setWindowTitle('Toolbar')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()