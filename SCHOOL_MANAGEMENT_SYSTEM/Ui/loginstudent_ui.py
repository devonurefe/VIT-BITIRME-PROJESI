# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Muhammed\OneDrive\Masaüstü\VIT BITIRME PROJESI\SCHOOL_MANAGEMENT_SYSTEM\Ui\loginstudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentWindow(object):
    def setupUi(self, StudentWindow):
        StudentWindow.setObjectName("StudentWindow")
        StudentWindow.resize(800, 600)
        StudentWindow.setMinimumSize(QtCore.QSize(800, 600))
        StudentWindow.setMaximumSize(QtCore.QSize(800, 600))
        StudentWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(StudentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sloginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.sloginbutton.setGeometry(QtCore.QRect(320, 330, 171, 28))
        self.sloginbutton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(143, 106, 185);\n"
"    color: rgb(245, 240, 218);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(115, 80, 139);\n"
"    color: rgb(245, 240, 218);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(81, 65, 108);\n"
"    padding-left:5px;\n"
"    color: rgb(245, 240, 218);\n"
"    padding-top:5px;\n"
"}")
        self.sloginbutton.setObjectName("sloginbutton")
        self.snumberline = QtWidgets.QLineEdit(self.centralwidget)
        self.snumberline.setGeometry(QtCore.QRect(270, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.snumberline.setFont(font)
        self.snumberline.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.snumberline.setObjectName("snumberline")
        self.spasswordline = QtWidgets.QLineEdit(self.centralwidget)
        self.spasswordline.setGeometry(QtCore.QRect(270, 260, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spasswordline.setFont(font)
        self.spasswordline.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.spasswordline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.spasswordline.setObjectName("spasswordline")
        self.sbackbutton = QtWidgets.QPushButton(self.centralwidget)
        self.sbackbutton.setGeometry(QtCore.QRect(320, 380, 171, 28))
        self.sbackbutton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(143, 106, 185);\n"
"    color: rgb(245, 240, 218);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(115, 80, 139);\n"
"    color: rgb(245, 240, 218);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(81, 65, 108);\n"
"    padding-left:5px;\n"
"    color: rgb(245, 240, 218);\n"
"    padding-top:5px;\n"
"}")
        self.sbackbutton.setObjectName("sbackbutton")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(170, 300, 460, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.message.setFont(font)
        self.message.setStyleSheet("color:  rgb(143, 106, 185);")
        self.message.setText("")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 400, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  rgb(143, 106, 185);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 160, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:  rgb(143, 106, 185);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 800, 600))
        self.label.setStyleSheet("background-color: rgb(172, 223, 230);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.sloginbutton.raise_()
        self.snumberline.raise_()
        self.spasswordline.raise_()
        self.sbackbutton.raise_()
        self.message.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        StudentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        StudentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentWindow)
        self.statusbar.setObjectName("statusbar")
        StudentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StudentWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentWindow)

    def retranslateUi(self, StudentWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentWindow.setWindowTitle(_translate("StudentWindow", "MainWindow"))
        self.sloginbutton.setText(_translate("StudentWindow", "LOGIN"))
        self.snumberline.setPlaceholderText(_translate("StudentWindow", "STUDENT NUMBER"))
        self.spasswordline.setPlaceholderText(_translate("StudentWindow", "PASSWORD"))
        self.sbackbutton.setText(_translate("StudentWindow", "BACK"))
        self.label_2.setText(_translate("StudentWindow", "TYPING SCHOOL"))
        self.label_3.setText(_translate("StudentWindow", "STUDENT LOGIN"))
