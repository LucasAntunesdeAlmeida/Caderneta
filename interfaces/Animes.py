import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon

class Animes(QMainWindow):
    def __init__(self, parent=None):
        super(Animes, self).__init__(parent)
        self.title = 'Caderneta de Animes'
        self.width = 205
        self.height = 200
        self.initUI()

    def initUI(self):
        # Init Window
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
