'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-10 14:04:22
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-10 14:17:26
FilePath: /pyqt6/Layout_management/box_layout.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: box_layout.py



import sys
from PyQt6.QtWidgets import (QWidget, QPushButton,
        QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
    
        hbox = QHBoxLayout()    # 创建一个水平布局
        hbox.addStretch(1)      # 在两个按钮之前插入一个伸缩空间
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()    # 创建一个垂直布局
        vbox.addStretch(1)      # 在两个按钮之前插入一个伸缩空间
        vbox.addLayout(hbox)

        self.setLayout(vbox)    # 将垂直布局放到窗口中

        self.setGeometry(10, 10, 350, 250)
        self.setWindowTitle('Buttons')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()