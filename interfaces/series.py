import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon

class Series(QMainWindow):
    def __init__(self, parent=None):
        super(Series, self).__init__(parent)
        self.titulo = 'Caderneta de Series'
        self.largura = 205
        self.altura = 200
        self.initUI()

    def initUI(self):
        # Inicia a janela
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.largura, self.altura)
