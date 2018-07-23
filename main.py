import os
import sys
from interfaces.selecao import *

sys.path.insert(0, './interfaces')
print(sys.path)

if __name__ == '__main__':
    os.system("bash CreateDate.sh")
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
