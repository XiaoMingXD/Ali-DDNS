from MainUI import *
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class MainWind(QWidget, Ui_Main):
    def __init__(self):
        super(MainWind, self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWind()
    w.show()
    sys.exit(app.exec_()) 

"""
    app = QApplication(sys.argv)
"""
