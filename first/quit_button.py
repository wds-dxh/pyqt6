'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-08 23:23:31
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 09:43:11
FilePath: /pyqt6/first/quit_button.py
Description: 使用按钮退出应用程序
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: quit_button.py
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)# 传递的参数是一个槽，这个槽是应用程序的quit()方法
        qbtn.resize(qbtn.sizeHint())    # sizeHint()方法提供了一个默认的按钮大小
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)    #设置窗口的位置和大小
        self.setWindowTitle('Quit button')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()