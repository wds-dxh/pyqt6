'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-07 20:06:37
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 09:24:43
FilePath: /pyqt6/first/tooltip.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: tooltip.py


import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt6.QtGui import QFont

"""
DeprecationWarning: sipPyTypeDict() is deprecated, the extension module should use sipPyTypeDictRef() instead

阿里源: pip install --upgrade sip -i https://mirrors.aliyun.com/pypi/simple/
"""
class Example(QWidget):
    def __init__(self):
        super().__init__()  #调用父类的构造函数，就不用写QWidget.__init__(self)
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))    #设置提示框的字体

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())#sizeHint是系统提供的一个默认大小，这里是按钮的大小
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()