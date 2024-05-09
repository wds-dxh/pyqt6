'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-08 18:13:22
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-08 18:26:30
FilePath: \pyqt6\Qlabel\QLineEdit加载.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
from PyQt6.QtWidgets import QApplication, QLineEdit
from PyQt6 import uic
import sys
from PyQt6.QtGui import QValidator, QIntValidator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("QLineEdit单行文本.ui")
    myLineEdit: QLineEdit = ui.lineEdit
    myLineEdit2: QLineEdit = ui.lineEdit_2

    myLineEdit.setValidator(QIntValidator(0, 100))
    myLineEdit.setFocus()


    ui.show()
    sys.exit(app.exec())















