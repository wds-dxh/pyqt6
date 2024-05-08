import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6 import uic


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("Qlabel.ui")
    myLabel: QLabel = ui.label # 获取label对象
    print(myLabel.text()) # 打印label文本值
    ui.show()
    sys.exit(app.exec())