'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-09 14:43:07
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 15:06:31
FilePath: /pyqt6/menus_and_toolbars/submenu.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
# !/usr/bin/python
# file: submenu.py
import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        menubar.setNativeMenuBar(False)
         # 为了在macOS上显示菜单栏，我们需要调用setNativeMenuBar()方法并传递False参数。

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)   # 创建一个QAction对象
        impMenu.addAction(impAct)

        newAct = QAction('New', self)   #flieMenu添加一个新的QAction对象,一级菜单

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)     # 添加impMenu到fileMenu,impMenu是fileMenu的子菜单,有一个动作impAct

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Submenu')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()