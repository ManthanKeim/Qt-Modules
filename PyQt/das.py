import sys
from PyQt5 import QtWidgets, QtGui


def careless(self):
    s = self.name.text()
    f_name = s.split("/")[-1]
    request.urlretrieve(s, f_name)


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l1.setText("HELLO WORLD")
    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap("1200px-Bugatti_Chiron_IMG_0087.jpg"))
    w.setWindowTitle("LESSO N2 ")
    #l3 = QtWidgets.QTextEdit("ENTER URL")
    #l4 = QtWidgets.QPushButton("DOWNLOAD")
    w.setGeometry(100, 100 , 300 , 200)
    l1.move(130,20)
    l2.move(120 ,90)
    w.show()
    sys.exit(app.exec_())


window()
