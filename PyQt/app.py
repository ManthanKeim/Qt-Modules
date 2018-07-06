from PyQt5 import QtWidgets
from parentdialog import ParentDialog

app = QtWidgets.QApplication([])
pr = ParentDialog()

pr.show()

exit(app.exec())
