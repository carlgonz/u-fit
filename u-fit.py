#!/usr/bin/env python3

__author__ = 'cgonzalez'

import sys
from PyQt4 import QtGui

# sys.path.append("src/python/")
from u_fit.main import Main

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    gui = Main()
    gui.show()
    sys.exit(app.exec_())