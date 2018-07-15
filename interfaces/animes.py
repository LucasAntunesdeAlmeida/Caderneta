import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon

class Animes(QMainWindow):
    def __init__(self, parent=None):
        super(Animes, self).__init__(parent)
        self.titulo = 'Caderneta de Animes'
        self.largura = 205
        self.altura = 200
        self.initUI()

    def initUI(self):
        # Inicia a janela
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.largura, self.altura)
