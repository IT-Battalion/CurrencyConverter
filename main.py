import sys

from PyQt6.QtWidgets import QApplication

from controller import Controller

if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    sys.exit(app.exec())

