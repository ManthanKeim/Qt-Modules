import sys
from PyQt5 import QtWidgets,QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b=QtWidgets.QPushButton("Look at me ")
    l=QtWidgets.QLabel("MAI HOON BE")

    hbox = QtWidgets.QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(l)
    hbox.addStretch()
    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap("1.jpg"))

    vbox = QtWidgets.QVBoxLayout()


    vbox.addWidget(b)
    w.setLayout(vbox)
    vbox.addLayout(hbox)
    w.setWindowTitle("HELLO")
    w.show()
    sys.exit(app.exec_())

window()
