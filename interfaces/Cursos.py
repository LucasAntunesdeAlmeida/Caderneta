import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from interfaces.TabelaMangas import *

class Cursos(QMainWindow):
    def __init__(self, parent=None):
        super(Cursos, self).__init__(parent)
        self.titulo = 'Caderneta de Cursos'
        self.largura = 515
        self.altura = 800
        self.initUI()

    def initUI(self):
        # Inicia a janela
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.largura, self.altura)

        # Barra de busca
        self.busca = QLineEdit(self)
        self.busca.move(20, 50)
        self.busca.setText('')
        self.busca.resize(300,30)

        # Cria botao de procura
        self.botaoMangas = QPushButton('Procurar', self)
        self.botaoMangas.move(330, 50)
        self.botaoMangas.resize(166, 30)
        self.botaoMangas.clicked.connect(self.procura)

        # Cria botao de ajuda
        self.botaoAjuda = QPushButton('ajuda', self)
        self.botaoAjuda.move(330, 10)
        self.botaoAjuda.resize(166, 30)
        self.botaoAjuda.clicked.connect(self.ajuda)

        # Cria botao de adicionar
        self.botaoAdicionar = QPushButton('adicionar', self)
        self.botaoAdicionar.move(330, 90)
        self.botaoAdicionar.resize(166, 30)
        self.botaoAdicionar.clicked.connect(self.adicionar)

        # Cria botao de remover
        self.botaoRemover = QPushButton('remover', self)
        self.botaoRemover.move(330, 130)
        self.botaoRemover.resize(166, 30)
        self.botaoRemover.clicked.connect(self.remover)

        self.tabela = TabelaMangas(self)

    def procura(self):
        pass

    def ajuda(self):
        pass

    def adicionar(self):
        pass

    def remover(self):
        pass
