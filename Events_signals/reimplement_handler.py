'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-10 14:40:57
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-10 14:41:59
FilePath: /pyqt6/Events_signals/reimplement_handler.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: reimplement_handler.py


import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication
   
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Event handler')
        self.show()


    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()