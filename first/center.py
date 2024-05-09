'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-09 09:48:57
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 14:17:15
FilePath: /pyqt6/first/center.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: center.py


import sys
from PyQt6.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(350, 250)
        self.center()

        self.setWindowTitle('Center')
        self.show()
        print("show")

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        print(cp)

        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()