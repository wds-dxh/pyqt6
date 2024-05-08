'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-07 19:29:31
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-07 20:02:36
FilePath: /pyqt6/first/simple.py
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
from PyQt6.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget() # 创建一个窗口
    w.resize(250, 200)
    w.move(100, 300)

    w.setWindowTitle('title')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()