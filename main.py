import sys
sys.path.insert(0, './interfaces')
print(sys.path)
from selecao import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Window()
    sys.exit(app.exec_())
