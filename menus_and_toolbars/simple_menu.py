'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-09 14:30:32
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 14:30:35
FilePath: /pyqt6/menus_and_toolbars/simple_menu.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: simple_menu.py


import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.initUI()


    def initUI(self):

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')    # 状态栏提示
        exitAct.triggered.connect(QApplication.instance().quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('close')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple menu')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()