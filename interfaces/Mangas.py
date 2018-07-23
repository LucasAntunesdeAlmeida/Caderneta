import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from interfaces.TabelaMangas import *

class Mangas(QMainWindow):
    def __init__(self, parent=None):
        super(Mangas, self).__init__(parent)
        self.title = 'Caderneta de Mangas'
        self.width = 515
        self.height = 800
        self.initUI()

    def initUI(self):
        # Init Window
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # Search bar
        self.lineSearch = QLineEdit(self)
        self.lineSearch.move(20, 50)
        self.lineSearch.setText('')
        self.lineSearch.resize(300,30)

        # Create Search's button
        self.buttonSearch = QPushButton('Search', self)
        self.buttonSearch.move(330, 50)
        self.buttonSearch.resize(166, 30)
        self.buttonSearch.clicked.connect(self.search)

        # Create Help's button
        self.buttonHelp = QPushButton('Help', self)
        self.buttonHelp.move(330, 10)
        self.buttonHelp.resize(166, 30)
        self.buttonHelp.clicked.connect(self.help)

        # Create Add's button
        self.buttonAdd = QPushButton('Add', self)
        self.buttonAdd.move(330, 90)
        self.buttonAdd.resize(166, 30)
        self.buttonAdd.clicked.connect(self.add)

        # Create Remove's button
        self.buttonRemove = QPushButton('Remove', self)
        self.buttonRemove.move(330, 130)
        self.buttonRemove.resize(166, 30)
        self.buttonRemove.clicked.connect(self.remove)

        self.table = TabelaMangas(self)

    def search(self):
        pass

    def help(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass
