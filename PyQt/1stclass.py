from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

dia = QtWidgets.QDialog()

layout = QtWidgets.QVBoxLayout()
name = QtWidgets.QLabel("AUR KAISA HAI")
name2 = QtWidgets.QLabel("BADIA BHAI")
b = QtWidgets.QPushButton("PUSH ME ")
c = QtWidgets.QLineEdit("WRITE HERE")
d = QtWidgets.QDateEdit()

layout.addWidget(name)
layout.addWidget(b)
layout.addWidget(c)
layout.addWidget(d)
layout.addWidget(name2)
dia.setLayout(layout)
dia.show()

app.exec_()