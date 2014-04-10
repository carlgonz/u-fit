__author__ = 'cgonzalez'

import sys
import os
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
        self.x = []
        self.y = []

        #UI settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Signals
        self.ui.update_button.clicked.connect(self.update_plot)
        self.ui.datafile_button.clicked.connect(self.select_file)

        self.ui.statusbar.showMessage("Connecting...", 10000)

        plot_html = self._plotly.iplot(self.x, self.y, filename='_',
                                       overwrite=True)
        self.ui.plot_webview.setContent(plot_html)

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
        percentil = self.ui.datasize_spinbox.value()
        return reg.regression(percentil)

    def update_plot(self):
        datafile = self.ui.datafile_line.text()
        self.load_data(datafile)

        [m, c, i, step] = self.adjust()

        status = "m:{0}, c:{1}, i:{2}, step:{3}".format(m, c, i, step)
        self.ui.statusbar.showMessage("Done. "+status+". Loading graph...",
                                      10000)

        y_adj = [c, self.x[0]*m+c, self.x[-1]*m+c]

        text_result = "f(x)={0:.2}*x{1:+.2}".format(m, c)

        scatter = {'x': self.x,
                   'y': self.y,
                   'name': 'Experimental data',
                   'type': 'scatter',
                   'mode': 'markers'}

        used = {'x': self.x[i:i+step],
                   'y': self.y[i:i+step],
                   'name': 'Used data',
                   'type': 'scatter',
                   'mode': 'markers'}

        adjust = {'x': [0, self.x[0], self.x[-1]],
                  'y': y_adj,
                  'name': 'Fit: '+text_result,
                  'type': 'scatter',
                  'mode': 'lines'}

        layout = {'xaxis': {'title': 'Shear rate'},
                  'yaxis': {'title': 'Shear stress'},
                  'title': os.path.basename(datafile),
                  'legend': {'x': 0, 'y': 1, 'opacity': 0.4}}

        plot_html = self._plotly.iplot([scatter, used, adjust], layout=layout,
                                       filename=os.path.basename(datafile),
                                       fileopt='overwrite',
                                       world_readable=True)

        self.ui.plot_webview.setContent(plot_html)
        self.ui.statusbar.showMessage("Graph loaded.", 5000)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    gui = Main()
    gui.show()
    sys.exit(app.exec_())