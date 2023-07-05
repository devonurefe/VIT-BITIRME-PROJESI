from PyQt5 import QtWidgets, uic


class EntryWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(EntryWindow, self).__init__()
        uic.loadUi(
            r"C:\Users\fujitsu\Documents\Software Development\VIT BITIRME PROJESI\SCHOOL_MANAGEMENT_SYSTEM\vit deneme\Ui\entry.ui", self)
        self.show()
