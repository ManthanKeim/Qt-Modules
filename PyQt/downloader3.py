import sys
from PyQt5.QtWidgets import QWidget, QProgressBar , QPushButton , QApplication , QLineEdit , QLabel
from PyQt5.QtCore import QBasicTimer
# from random import randrange


# name = randrange(1,1000)

class TW(QWidget):
    def __init__(self):
        super().__init__()

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 40 , 200 , 25)




        self.btn = QPushButton("Start1" , self)
        self.btn.move(40 , 80)
        self.btn.clicked.connect(self.start)

        self.t = QLineEdit(self)
        self.t.move(40 , 200)

        self.btn1 = QPushButton("Start", self)
        self.btn1.move(40, 80)
        self.btn1.clicked.connect(self.start)

        self.timer = QBasicTimer()
        self.step = 0


    def start(self):
        if self.timer.isActive():
            URL = self.t.text()
            fname = URL.split("/")[-1] + ".jpg"
            Thread(target=lambda: request.urlretrieve(URL, fname,hook)).start()
            self.btn.setText("DOWNLOADING")
        else:
            self.timer.start(100, self)
            self.btn.setText("STOP")

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("DOWNLOADED")
            return
        self.timer.start(100, self)
        self.btn.setText("STOP")

    def hook(f=0, s=0, t=0):
        total = f * s
        print(int(total / t * 100))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tw = TW()
    tw.show()
    sys.exit(app.exec_())