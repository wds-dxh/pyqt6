'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-09 14:21:44
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 14:23:18
FilePath: /pyqt6/menus_and_toolbars/statusbar.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: statusbar.py

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(10, 10, 350, 250)    #设置窗口位置和大小
        self.setWindowTitle('Statusbar')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()