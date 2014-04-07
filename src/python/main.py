__author__ = 'cgonzalez'

import sys
import plotly
import numpy as np
from modules import regression

from PyQt4 import QtGui
from PyQt4 import QtCore

from forms.MainWindow_UI import *


class Main(QtGui.QMainWindow):
    def __init__(self):
        """
        Main window initialization
        """

        QtGui.QMainWindow.__init__(self)

        #Instance variables
        self._plotly = plotly.plotly("cgnozalez", "nu091rxas4")
        self.x = None
        self.y = None

        #UI settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Signals
        self.ui.update_button.clicked.connect(self.update_plot)
        self.ui.datafile_button.clicked.connect(self.select_file)

    def select_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open datafile",
                                                     QtCore.QDir.currentPath(),
                                                     "Text files (*.txt);"
                                                     "Comma separated (*.csv);"
                                                     "All files (*.*)")

        self.ui.datafile_line.setText(filename)

    def load_data(self, filename, cols=(1, 2)):
        data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=cols)
        self.x = data[:, 0]
        self.y = data[:, 1]

    def adjust(self):
        reg = regression.Regression(self.x, self.y)
        percentil = self.ui.datasize_slider.value()
        return reg.regression(percentil)

    def update_plot(self):
        datafile = self.ui.datafile_line.text()
        self.load_data(datafile)

        [m, c] = self.adjust()
        y_adj = [self.x[0]*m+c, self.x[-1]*m+c]

        scatter = {'x': self.x,
                   'y': self.y,
                   'type': 'scatter',
                   'mode': 'markers'}

        adjust = {'x': [self.x[0], self.x[-1]],
                  'y': y_adj,
                  'type': 'scatter',
                  'mode': 'lines'}

        plot_html = self._plotly.iplot([scatter, adjust])
        self.ui.plot_webview.setContent(plot_html)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    gui = Main()
    gui.show()
    sys.exit(app.exec_())