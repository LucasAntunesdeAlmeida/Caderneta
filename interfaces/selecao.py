import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from interfaces.mangas import *
from interfaces.animes import *
from interfaces.series import *
from interfaces.filmes import *
from interfaces.Novels import *
from interfaces.Cursos import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.titulo = 'Caderneta'
        self.largura = 370
        self.altura = 280
        self.initUI()

    def initUI(self):
        # Inicia a janela
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.largura, self.altura)

        # Cria Texto acima dos botoes
        self.lbl = QLabel(self)
        self.lbl.setText('Escolha o tipo de Caderneta:')
        self.lbl.resize(180, 30)
        self.lbl.move(20, 10)

        #texto quant finalizados
        self.lbl = QLabel(self)
        self.lbl.setText('Finalizados:')
        self.lbl.resize(100, 30)
        self.lbl.move(220, 10)

        #texto quant total
        self.lbl = QLabel(self)
        self.lbl.setText('Total:')
        self.lbl.resize(50, 30)
        self.lbl.move(320, 10)

        # Cria botao de Mangas
        self.botaoMangas = QPushButton('Mangas', self)
        self.botaoMangas.move(20, 40)
        self.botaoMangas.resize(166, 30)
        self.subJanelaMangas = Mangas(self)
        self.botaoMangas.clicked.connect(self.mangas)

        # Cria botao de Novels
        self.botaoNovels = QPushButton('Novels', self)
        self.botaoNovels.move(20, 80)
        self.botaoNovels.resize(166, 30)
        self.subJanelaNovels = Novels(self)
        self.botaoNovels.clicked.connect(self.novels)

        # Cria botao de Animes
        self.botaoAnimes = QPushButton('Animes', self)
        self.botaoAnimes.move(20, 120)
        self.botaoAnimes.resize(166, 30)
        self.subJanelaAnimes = Animes(self)
        self.botaoAnimes.clicked.connect(self.animes)

        # Cria botao de Series
        self.botaoSeries = QPushButton('Series', self)
        self.botaoSeries.move(20, 160)
        self.botaoSeries.resize(166, 30)
        self.subJanelaSeries = Series(self)
        self.botaoSeries.clicked.connect(self.series)

        # Cria botao de Filmes
        self.botaoFilmes = QPushButton('Filmes', self)
        self.botaoFilmes.move(20, 200)
        self.botaoFilmes.resize(166, 30)
        self.subJanelaFilmes = Filmes(self)
        self.botaoFilmes.clicked.connect(self.filmes)

        # Cria botao de Cursos
        self.botaoCursos = QPushButton('Cursos', self)
        self.botaoCursos.move(20, 240)
        self.botaoCursos.resize(166, 30)
        self.subJanelaCursos = Cursos(self)
        self.botaoCursos.clicked.connect(self.cursos)

        self.show()

    def mangas(self):
        self.subJanelaMangas.show()
        self.subJanelaMangas.tabela.show()

    def novels(self):
        self.subJanelaNovels.show()

    def animes(self):
        self.subJanelaAnimes.show()

    def series(self):
        self.subJanelaSeries.show()

    def filmes(self):
        self.subJanelaFilmes.show()

    def cursos(self):
        self.subJanelaCursos.show()
