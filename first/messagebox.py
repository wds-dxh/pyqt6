'''
Author: wds-dxh wdsnpshy@163.com
Date: 2024-05-09 09:43:57
LastEditors: wds-dxh wdsnpshy@163.com
LastEditTime: 2024-05-09 09:45:26
FilePath: /pyqt6/first/messagebox.py
Description: 
微信: 15310638214 
邮箱：wdsnpshy@163.com 
Copyright (c) 2024 by ${wds-dxh}, All Rights Reserved. 
'''
#!/usr/bin/python
# file: messagebox.py


import sys
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):    # 重写closeEvent()方法，这个方法会在用户关闭窗口时调用

        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()