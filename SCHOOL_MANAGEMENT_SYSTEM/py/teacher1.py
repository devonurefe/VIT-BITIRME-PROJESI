# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color:rgb(172, 223, 230);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tname_label1 = QtWidgets.QLabel(self.centralwidget)
        self.tname_label1.setGeometry(QtCore.QRect(10, 20, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tname_label1.setFont(font)
        self.tname_label1.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.tname_label1.setObjectName("tname_label1")
        self.tname_label = QtWidgets.QLabel(self.centralwidget)
        self.tname_label.setGeometry(QtCore.QRect(135, 20, 225, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tname_label.setFont(font)
        self.tname_label.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.tname_label.setText("")
        self.tname_label.setObjectName("tname_label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 761, 411))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color:  rgb(143, 106, 185);\n"
"background-color: rgb(172, 223, 230);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lesson_combo = QtWidgets.QComboBox(self.tab)
        self.lesson_combo.setGeometry(QtCore.QRect(10, 300, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lesson_combo.setFont(font)
        self.lesson_combo.setStyleSheet("background-color: rgb(245, 240, 218);")
        self.lesson_combo.setObjectName("lesson_combo")
        self.add_button = QtWidgets.QPushButton(self.tab)
        self.add_button.setGeometry(QtCore.QRect(370, 300, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("QPushButton{\n"
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
        self.add_button.setObjectName("add_button")
        self.lesson_combo_6 = QtWidgets.QComboBox(self.tab)
        self.lesson_combo_6.setGeometry(QtCore.QRect(10, 340, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lesson_combo_6.setFont(font)
        self.lesson_combo_6.setStyleSheet("\n"
"background-color: rgb(245, 240, 218);")
        self.lesson_combo_6.setObjectName("lesson_combo_6")
        self.remove_button_2 = QtWidgets.QPushButton(self.tab)
        self.remove_button_2.setGeometry(QtCore.QRect(370, 340, 110, 30))
        self.remove_button_2.setStyleSheet("QPushButton{\n"
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
        self.remove_button_2.setObjectName("remove_button_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(-6, -5, 761, 391))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lesson_widget = QtWidgets.QTableWidget(self.tab)
        self.lesson_widget.setGeometry(QtCore.QRect(10, 20, 741, 271))
        self.lesson_widget.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.lesson_widget.setObjectName("lesson_widget")
        self.lesson_widget.setColumnCount(3)
        self.lesson_widget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lesson_widget.setHorizontalHeaderItem(2, item)
        self.lesson_widget.horizontalHeader().setDefaultSectionSize(240)
        self.lesson_widget.verticalHeader().setDefaultSectionSize(47)
        self.counterror = QtWidgets.QLabel(self.tab)
        self.counterror.setGeometry(QtCore.QRect(480, 300, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.counterror.setFont(font)
        self.counterror.setStyleSheet("color:  rgb(143, 106, 185);")
        self.counterror.setText("")
        self.counterror.setAlignment(QtCore.Qt.AlignCenter)
        self.counterror.setObjectName("counterror")
        self.label_2.raise_()
        self.lesson_combo.raise_()
        self.add_button.raise_()
        self.lesson_combo_6.raise_()
        self.remove_button_2.raise_()
        self.lesson_widget.raise_()
        self.counterror.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lesson_combo_2 = QtWidgets.QComboBox(self.tab_2)
        self.lesson_combo_2.setGeometry(QtCore.QRect(100, 10, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lesson_combo_2.setFont(font)
        self.lesson_combo_2.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"")
        self.lesson_combo_2.setObjectName("lesson_combo_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.student_combo = QtWidgets.QComboBox(self.tab_2)
        self.student_combo.setGeometry(QtCore.QRect(100, 50, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.student_combo.setFont(font)
        self.student_combo.setStyleSheet("background-color: rgb(245, 240, 218);")
        self.student_combo.setObjectName("student_combo")
        self.show_button = QtWidgets.QPushButton(self.tab_2)
        self.show_button.setGeometry(QtCore.QRect(100, 90, 350, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.show_button.setFont(font)
        self.show_button.setStyleSheet("QPushButton{\n"
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
        self.show_button.setObjectName("show_button")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 290, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 330, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.name = QtWidgets.QLabel(self.tab_2)
        self.name.setGeometry(QtCore.QRect(150, 130, 225, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.name.setText("")
        self.name.setObjectName("name")
        self.gender = QtWidgets.QLabel(self.tab_2)
        self.gender.setGeometry(QtCore.QRect(150, 170, 225, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gender.setFont(font)
        self.gender.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.gender.setText("")
        self.gender.setObjectName("gender")
        self.birth = QtWidgets.QLabel(self.tab_2)
        self.birth.setGeometry(QtCore.QRect(150, 210, 225, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.birth.setFont(font)
        self.birth.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.birth.setText("")
        self.birth.setObjectName("birth")
        self.ok_button = QtWidgets.QPushButton(self.tab_2)
        self.ok_button.setGeometry(QtCore.QRect(470, 10, 110, 30))
        self.ok_button.setStyleSheet("QPushButton{\n"
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
        self.ok_button.setObjectName("ok_button")
        self.midterm = QtWidgets.QLineEdit(self.tab_2)
        self.midterm.setGeometry(QtCore.QRect(150, 250, 225, 30))
        self.midterm.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.midterm.setObjectName("midterm")
        self.final_2 = QtWidgets.QLineEdit(self.tab_2)
        self.final_2.setGeometry(QtCore.QRect(150, 290, 225, 30))
        self.final_2.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.final_2.setObjectName("final_2")
        self.attendance = QtWidgets.QLineEdit(self.tab_2)
        self.attendance.setGeometry(QtCore.QRect(150, 330, 225, 30))
        self.attendance.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"color:  rgb(143, 106, 185);")
        self.attendance.setObjectName("attendance")
        self.edit_button = QtWidgets.QPushButton(self.tab_2)
        self.edit_button.setGeometry(QtCore.QRect(470, 330, 110, 30))
        self.edit_button.setStyleSheet("QPushButton{\n"
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
        self.edit_button.setObjectName("edit_button")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 761, 391))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.lesson_combo_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.student_combo.raise_()
        self.show_button.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.name.raise_()
        self.gender.raise_()
        self.birth.raise_()
        self.ok_button.raise_()
        self.midterm.raise_()
        self.final_2.raise_()
        self.attendance.raise_()
        self.edit_button.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.add = QtWidgets.QWidget(self.tab_4)
        self.add.setGeometry(QtCore.QRect(10, 70, 370, 201))
        self.add.setStyleSheet("background:rgb(224, 255, 251)")
        self.add.setObjectName("add")
        self.lesson_combo_4 = QtWidgets.QComboBox(self.add)
        self.lesson_combo_4.setGeometry(QtCore.QRect(70, 40, 175, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lesson_combo_4.setFont(font)
        self.lesson_combo_4.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"")
        self.lesson_combo_4.setObjectName("lesson_combo_4")
        self.label_25 = QtWidgets.QLabel(self.add)
        self.label_25.setGeometry(QtCore.QRect(90, 0, 185, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_27 = QtWidgets.QLabel(self.add)
        self.label_27.setGeometry(QtCore.QRect(0, 40, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.add)
        self.label_28.setGeometry(QtCore.QRect(0, 110, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.student_combo_3 = QtWidgets.QComboBox(self.add)
        self.student_combo_3.setGeometry(QtCore.QRect(70, 110, 175, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.student_combo_3.setFont(font)
        self.student_combo_3.setStyleSheet("background-color: rgb(245, 240, 218);")
        self.student_combo_3.setObjectName("student_combo_3")
        self.add_button_2 = QtWidgets.QPushButton(self.add)
        self.add_button_2.setGeometry(QtCore.QRect(250, 110, 110, 28))
        self.add_button_2.setStyleSheet("QPushButton{\n"
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
        self.add_button_2.setObjectName("add_button_2")
        self.ok_button_3 = QtWidgets.QPushButton(self.add)
        self.ok_button_3.setGeometry(QtCore.QRect(250, 40, 110, 28))
        self.ok_button_3.setStyleSheet("QPushButton{\n"
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
        self.ok_button_3.setObjectName("ok_button_3")
        self.remove = QtWidgets.QWidget(self.tab_4)
        self.remove.setGeometry(QtCore.QRect(390, 70, 370, 201))
        self.remove.setStyleSheet("background:rgb(224, 255, 251)")
        self.remove.setObjectName("remove")
        self.label_26 = QtWidgets.QLabel(self.remove)
        self.label_26.setGeometry(QtCore.QRect(90, 0, 185, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.lesson_combo_5 = QtWidgets.QComboBox(self.remove)
        self.lesson_combo_5.setGeometry(QtCore.QRect(70, 40, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lesson_combo_5.setFont(font)
        self.lesson_combo_5.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"")
        self.lesson_combo_5.setObjectName("lesson_combo_5")
        self.student_combo_4 = QtWidgets.QComboBox(self.remove)
        self.student_combo_4.setGeometry(QtCore.QRect(70, 110, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.student_combo_4.setFont(font)
        self.student_combo_4.setStyleSheet("background-color: rgb(245, 240, 218);\n"
"")
        self.student_combo_4.setObjectName("student_combo_4")
        self.label_29 = QtWidgets.QLabel(self.remove)
        self.label_29.setGeometry(QtCore.QRect(0, 40, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.remove)
        self.label_30.setGeometry(QtCore.QRect(0, 110, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.remove_button = QtWidgets.QPushButton(self.remove)
        self.remove_button.setGeometry(QtCore.QRect(250, 110, 110, 28))
        self.remove_button.setStyleSheet("QPushButton{\n"
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
        self.remove_button.setObjectName("remove_button")
        self.ok_button_2 = QtWidgets.QPushButton(self.remove)
        self.ok_button_2.setGeometry(QtCore.QRect(250, 40, 110, 28))
        self.ok_button_2.setStyleSheet("QPushButton{\n"
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
        self.ok_button_2.setObjectName("ok_button_2")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(-6, -5, 761, 391))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.counterror_2 = QtWidgets.QLabel(self.tab_4)
        self.counterror_2.setGeometry(QtCore.QRect(20, 280, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.counterror_2.setFont(font)
        self.counterror_2.setStyleSheet("color:  rgb(143, 106, 185);")
        self.counterror_2.setText("")
        self.counterror_2.setAlignment(QtCore.Qt.AlignCenter)
        self.counterror_2.setObjectName("counterror_2")
        self.label_12.raise_()
        self.add.raise_()
        self.remove.raise_()
        self.counterror_2.raise_()
        self.tabWidget.addTab(self.tab_4, "")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(680, 510, 110, 30))
        self.closebutton.setStyleSheet("QPushButton{\n"
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
        self.closebutton.setObjectName("closebutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 0, 821, 600))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.tabWidget.raise_()
        self.tname_label1.raise_()
        self.tname_label.raise_()
        self.closebutton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tname_label1.setText(_translate("MainWindow", "Teacher\'s name:"))
        self.add_button.setText(_translate("MainWindow", "ADD LESSON"))
        self.remove_button_2.setText(_translate("MainWindow", "REMOVE LESSON"))
        item = self.lesson_widget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.lesson_widget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.lesson_widget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.lesson_widget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.lesson_widget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.lesson_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LESSON"))
        item = self.lesson_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CLASS NAME"))
        item = self.lesson_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CAPACITY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Lessons"))
        self.label_3.setText(_translate("MainWindow", "Lesson:"))
        self.label_4.setText(_translate("MainWindow", "Student:"))
        self.show_button.setText(_translate("MainWindow", "SHOW STUDENT INFORMATION"))
        self.label_5.setText(_translate("MainWindow", "Student Name:"))
        self.label_6.setText(_translate("MainWindow", "Gender:"))
        self.label_7.setText(_translate("MainWindow", "Date of Birth:"))
        self.label_8.setText(_translate("MainWindow", "Midterm:"))
        self.label_9.setText(_translate("MainWindow", "Final:"))
        self.label_10.setText(_translate("MainWindow", "Attendance:"))
        self.ok_button.setText(_translate("MainWindow", "SHOW STUDENTS"))
        self.edit_button.setText(_translate("MainWindow", "EDIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Show student"))
        self.label_25.setText(_translate("MainWindow", "ADD"))
        self.label_27.setText(_translate("MainWindow", "Lesson:"))
        self.label_28.setText(_translate("MainWindow", "Students:"))
        self.add_button_2.setText(_translate("MainWindow", "ADD"))
        self.ok_button_3.setText(_translate("MainWindow", "SHOW STUDENTS"))
        self.label_26.setText(_translate("MainWindow", "REMOVE"))
        self.label_29.setText(_translate("MainWindow", "Lesson:"))
        self.label_30.setText(_translate("MainWindow", "Students:"))
        self.remove_button.setText(_translate("MainWindow", "REMOVE"))
        self.ok_button_2.setText(_translate("MainWindow", "SHOW STUDENTS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Add/Remove Student"))
        self.closebutton.setText(_translate("MainWindow", "CLOSE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
