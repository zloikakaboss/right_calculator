# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcul.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 400)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "    background: #121212;\n"
                                 "    font-size: 16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: transparent;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #666\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #888\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setFlat(True)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setFlat(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 2, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setFlat(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_1.setFlat(True)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setFlat(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 1, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setFlat(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 2, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setFlat(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 0, 2, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setFlat(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 2, 2, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setFlat(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 2, 3, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setFlat(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 3, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.new_function()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.pushButton_3.setText(_translate("MainWindow", "6"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_15.setText(_translate("MainWindow", "8"))
        self.pushButton_16.setText(_translate("MainWindow", "<-"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_18.setText(_translate("MainWindow", "4"))
        self.pushButton_19.setText(_translate("MainWindow", "7"))
        self.pushButton_20.setText(_translate("MainWindow", "3"))
        self.pushButton_21.setText(_translate("MainWindow", "9"))
        self.pushButton_22.setText(_translate("MainWindow", "*"))
        self.pushButton_23.setText(_translate("MainWindow", "="))
        self.pushButton.setText(_translate("MainWindow", "/"))

    def new_function(self, ):
        self.btn_1.clicked.connect(lambda: self.write(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write(self.btn_2.text()))
        self.pushButton_2.clicked.connect(lambda: self.write(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write(self.pushButton_3.text()))
        self.pushButton_7.clicked.connect(lambda: self.write(self.pushButton_7.text()))
        self.pushButton_14.clicked.connect(lambda: self.write(self.pushButton_14.text()))
        self.pushButton_15.clicked.connect(lambda: self.write(self.pushButton_15.text()))
        self.pushButton_18.clicked.connect(lambda: self.write(self.pushButton_18.text()))
        self.pushButton_19.clicked.connect(lambda: self.write(self.pushButton_19.text()))
        self.pushButton_20.clicked.connect(lambda: self.write(self.pushButton_20.text()))
        self.pushButton_21.clicked.connect(lambda: self.write(self.pushButton_21.text()))
        self.pushButton_22.clicked.connect(lambda: self.write(self.pushButton_22.text()))
        self.pushButton_23.clicked.connect(self.result)
        self.pushButton_16.clicked.connect(self.clear)

    def write(self, number):
        self.label.setText(self.label.text() + number)

    def result(self,):
        res = eval(self.label.text())
        self.lineEdit.setText(str(res))

    def clear(self,):
        text = self.label.text()[:-1]
        self.label.setText(text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
