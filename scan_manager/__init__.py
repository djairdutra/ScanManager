import sys

from PySide import QtGui

from .widgets import MainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
