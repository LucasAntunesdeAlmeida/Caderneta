import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from interfaces.Mangas import *
from interfaces.Animes import *
from interfaces.series import *
from interfaces.filmes import *
from interfaces.Novels import *
from interfaces.Cursos import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.title = 'Caderneta'
        self.width = 370
        self.height = 280
        self.initUI()

    def initUI(self):
        # Init Window
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # Create text above the buttons
        self.lblE = QLabel(self)
        self.lblE.setText('Choose the Option:')
        self.lblE.resize(180, 30)
        self.lblE.move(20, 10)

        # Create text above the finished quantities
        self.lblF = QLabel(self)
        self.lblF.setText('Finished:')
        self.lblF.resize(100, 30)
        self.lblF.move(220, 10)

        # Create text above the total quantities
        self.lblT = QLabel(self)
        self.lblT.setText('Total:')
        self.lblT.resize(50, 30)
        self.lblT.move(320, 10)

        # Create Mangas's button
        self.buttonMangas = QPushButton('Mangas', self)
        self.buttonMangas.move(20, 40)
        self.buttonMangas.resize(166, 30)
        self.subWindowMangas = Mangas(self)
        self.buttonMangas.clicked.connect(self.mangas)

        # Create Novels's button
        self.buttonNovels = QPushButton('Novels', self)
        self.buttonNovels.move(20, 80)
        self.buttonNovels.resize(166, 30)
        self.subWindowNovels = Novels(self)
        self.buttonNovels.clicked.connect(self.novels)

        # Create Animes's button
        self.buttonAnimes = QPushButton('Animes', self)
        self.buttonAnimes.move(20, 120)
        self.buttonAnimes.resize(166, 30)
        self.subWindowAnimes = Animes(self)
        self.buttonAnimes.clicked.connect(self.animes)

        # Create Series's button
        self.buttonSeries = QPushButton('Series', self)
        self.buttonSeries.move(20, 160)
        self.buttonSeries.resize(166, 30)
        self.subWindowSeries = Series(self)
        self.buttonSeries.clicked.connect(self.series)

        # Create Movies's button
        self.buttonMovies = QPushButton('Movies', self)
        self.buttonMovies.move(20, 200)
        self.buttonMovies.resize(166, 30)
        self.subWindowMovies = Filmes(self)
        self.buttonMovies.clicked.connect(self.movies)

        # Create Courses's button
        self.buttonCourses = QPushButton('Courses', self)
        self.buttonCourses.move(20, 240)
        self.buttonCourses.resize(166, 30)
        self.subWindowCourses = Cursos(self)
        self.buttonCourses.clicked.connect(self.courses)

        self.show()

    def mangas(self):
        self.subWindowMangas.show()

    def novels(self):
        self.subWindowNovels.show()

    def animes(self):
        self.subWindowAnimes.show()

    def series(self):
        self.subWindowSeries.show()

    def movies(self):
        self.subWindowMovies.show()

    def courses(self):
        self.subWindowCourses.show()
