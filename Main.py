from MainUI import *
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWind(QWidget, Ui_Main):
    def __init__(self):
        super(MainWind, self).__init__()
        self.setupUi(self)
        self.DebugC.stateChanged.connect(self.DebugCc)
        
    def DebugCc(self, state):
        print state
        if state == 2:
            self.resize(705, 303)
        else:
            self.resize(420, 303)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWind()
    w.show()
    sys.exit(app.exec_()) 
