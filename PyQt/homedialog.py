from PyQt5 import QtWidgets
import random
from urllib import request
from threading import Thread

name = random.randrange(1,1000)

class HomeDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.name = QtWidgets.QLabel("AUR KAISA HAI")
        self.name2 = QtWidgets.QLabel("DOWNLOADING")
        self.b = QtWidgets.QPushButton("PUSH ME ")

        self.b.clicked.connect(self.careless)
        self.c = QtWidgets.QLineEdit("")
        self.c.textChanged.connect(self.edited)
        d = QtWidgets.QDateEdit()

        layout.addWidget(self.name)
        layout.addWidget(self.b)
        layout.addWidget(self.c)
        layout.addWidget(d)
        layout.addWidget(self.name2)
        self.setLayout(layout)

    def edited(self, text):
        self.name.setText(text)

    def careless(self):
        URL =self.c.text()
        fname = str(name) + ".jpg"
        Thread(target=lambda: request.urlretrieve(URL, fname)).start()






