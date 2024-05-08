from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
import sys


from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 523)
        self.spinBox = QtWidgets.QSpinBox(parent=Form)
        self.spinBox.setGeometry(QtCore.QRect(200, 50, 81, 31))
        self.spinBox.setSingleStep(2)
        self.spinBox.setStepType(QtWidgets.QAbstractSpinBox.StepType.DefaultStepType)
        self.spinBox.setObjectName("spinBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.spinBox.setSuffix(_translate("Form", "   个"))
        self.spinBox.setPrefix(_translate("Form", "第  "))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(w)
    SpinBox = ui.spinBox
    #获得SpinBox的值
    print(SpinBox.value())

    w.show()
    sys.exit(app.exec())