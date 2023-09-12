from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton
#QApplication, QMainWindow, QWidget, QCalendarWidget, QLabel, QPushButton, QCheckBox, QSpinBox, QLCDNumber, QLineEdit, QSlider, QProgressBar
import pyqt_clarisse
import os

PROD = os.getenv('PROD')
SEQ = os.getenv('SEQ')
SHOT = os.getenv('SHOT')
SHOT_PATH = os.getenv('SHOT_PATH')

class ClarisseExporterEnv(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClarisseExporterEnv, self).__init__(parent)
        self.setWindowTitle('Change shot')
        self.resize(350, 150)

        self.nameLabel = QLabel(self)
        self.nameLabel.move(80, 5)
        self.nameLabel.setText('New Shot:')

        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(200, 32)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

        self.nameLabelShot = QLabel(self)
        self.nameLabelShot.move(80, 100)
        self.nameLabelShot.setText('Your current Shot : '+SHOT)


    def clickMethod(self):
        textSplit = self.line.text().split('_')
        print('Your new Shot: ' + self.line.text())
        os.environ["SEQ"] = textSplit[0]+'_'+textSplit[1]
        os.environ["SHOT"] = textSplit[0]+'_'+textSplit[1]+'_'+textSplit[2]
        nSHOT_PATH = os.path.join('/mnt/prod/',PROD,'sequence',textSplit[0]+'_'+textSplit[1],textSplit[0]+'_'+textSplit[1]+'_'+textSplit[2])
        os.environ["SHOT_PATH"] = nSHOT_PATH
        print(nSHOT_PATH)


if QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication.instance()
else:
    app = QtWidgets.QApplication(["Clarisse"])
submitter_windows = ClarisseExporterEnv()
submitter_windows.show()
pyqt_clarisse.exec_(app)


