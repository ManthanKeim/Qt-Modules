import sys
from PyQt5.QtWidgets import QWidget, QProgressBar , QPushButton , QApplication
from PyQt5.QtCore import QBasicTimer
from pprint import pprint

class TW(QWidget):
    def __init__(self):
        super().__init__()
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 40 , 200 , 25)

        self.btn = QPushButton("Start" , self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.start)

        self.timer = QBasicTimer()
        self.step = 0


    def start(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("Start")
        else:
            self.timer.start(100 , self)
            self.btn.setText("STOP")

    def timerEvent(self, event ):
        if self.step>=100:
            self.timer.stop()
            self.btn.setText("FINISHED")
            self.progressbar.reset()
            return
        self.step += 1
        self.progressbar.setValue(self.step)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tw = TW()
    tw.show()
    sys.exit(app.exec_())