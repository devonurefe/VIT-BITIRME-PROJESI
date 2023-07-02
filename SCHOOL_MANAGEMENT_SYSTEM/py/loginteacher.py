# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginteacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeacherWindow(object):
    def setupUi(self, TeacherWindow):
        TeacherWindow.setObjectName("TeacherWindow")
        TeacherWindow.resize(800, 600)
        TeacherWindow.setMinimumSize(QtCore.QSize(800, 600))
        TeacherWindow.setMaximumSize(QtCore.QSize(800, 600))
        TeacherWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(TeacherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tloginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.tloginbutton.setGeometry(QtCore.QRect(320, 330, 171, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tloginbutton.setFont(font)
        self.tloginbutton.setStyleSheet("QPushButton{\n"
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
        self.tloginbutton.setObjectName("tloginbutton")
        self.usernameline = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameline.setGeometry(QtCore.QRect(270, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usernameline.setFont(font)
        self.usernameline.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.usernameline.setObjectName("usernameline")
        self.tpasswordline = QtWidgets.QLineEdit(self.centralwidget)
        self.tpasswordline.setGeometry(QtCore.QRect(270, 260, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tpasswordline.setFont(font)
        self.tpasswordline.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.tpasswordline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tpasswordline.setObjectName("tpasswordline")
        self.tbackbutton = QtWidgets.QPushButton(self.centralwidget)
        self.tbackbutton.setGeometry(QtCore.QRect(320, 380, 171, 28))
        self.tbackbutton.setStyleSheet("QPushButton{\n"
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
        self.tbackbutton.setObjectName("tbackbutton")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setStyleSheet("background-color: rgb(172, 223, 230);")
        self.label.setText("")
        self.label.setObjectName("label")
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
        self.label.raise_()
        self.tloginbutton.raise_()
        self.usernameline.raise_()
        self.tpasswordline.raise_()
        self.tbackbutton.raise_()
        self.message.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        TeacherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TeacherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TeacherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TeacherWindow)
        self.statusbar.setObjectName("statusbar")
        TeacherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TeacherWindow)
        QtCore.QMetaObject.connectSlotsByName(TeacherWindow)

    def retranslateUi(self, TeacherWindow):
        _translate = QtCore.QCoreApplication.translate
        TeacherWindow.setWindowTitle(_translate("TeacherWindow", "MainWindow"))
        self.tloginbutton.setText(_translate("TeacherWindow", "LOGIN"))
        self.usernameline.setPlaceholderText(_translate("TeacherWindow", "USER NAME"))
        self.tpasswordline.setPlaceholderText(_translate("TeacherWindow", "PASSWORD"))
        self.tbackbutton.setText(_translate("TeacherWindow", "BACK"))
        self.label_2.setText(_translate("TeacherWindow", "TYPING SCHOOL"))
        self.label_3.setText(_translate("TeacherWindow", "TEACHER LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeacherWindow = QtWidgets.QMainWindow()
    ui = Ui_TeacherWindow()
    ui.setupUi(TeacherWindow)
    TeacherWindow.show()
    sys.exit(app.exec_())