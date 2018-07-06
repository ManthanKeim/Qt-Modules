from PyQt5 import QtWidgets
from homedialog import HomeDialog
class ParentDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        # name = QtWidgets.QLabel("AUR KAISA HAI")
        # name2 = QtWidgets.QLabel("BADIA BHAI")
        # b = QtWidgets.QPushButton("PUSH ME ")
        # c = QtWidgets.QLineEdit("WRITE HERE")
        # d = QtWidgets.QDateEdit()
        name = HomeDialog()
        name2 = HomeDialog()
        # layout.addWidget(name)
        # layout.addWidget(b)
        # layout.addWidget(c)
        # layout.addWidget(d)
        # layout.addWidget(name2)
        layout.addWidget(name)
        layout.addWidget(name2)
        self.setLayout(layout)
