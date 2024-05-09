from PyQt6.QtWidgets import QApplication, QLineEdit
from PyQt6 import uic
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("QLineEdit单行文本.ui")
    mylineedit: QLineEdit = ui.lineEdit
    mylineedit2: QLineEdit = ui.lineEdit_2
    mylineedit.setFocus()
    mylineedit.setPlaceholderText("请输入用户名")
    mylineedit2.setPlaceholderText("请输入密码")

    ui.show()
    sys.exit(app.exec())
