__author__ = 'cgonzalez'

import sys
import os
import plotly
import pygal
import numpy as np
from modules import regression
from pygal.style import RedBlueStyle as PlotStyle

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
        self.x = []
        self.y = []

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
        try:
            data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=cols)
            self.x = data[:, 0]
            self.y = data[:, 1]
        except FileNotFoundError:
            self.x = []
            self.y = []
            self.ui.statusbar.showMessage("File not found.", 5000)

    def adjust(self):
        reg = regression.Regression(self.x, self.y)
        percentil = self.ui.datasize_spinbox.value()
        return reg.regression(percentil)

    def update_plot(self):
        datafile = self.ui.datafile_line.text()
        self.load_data(datafile)

        if (len(self.x) == 0) or (len(self.y) == 0):
            return

        try:
            [m, c, r, i, step] = self.adjust()

        except Exception:
            self.ui.statusbar.showMessage("Error, please try again.", 2000)
            return

        status = "m:{0}, c:{1}, i:{2}, step:{3}".format(m, c, i, step)
        self.ui.statusbar.showMessage("Done. "+status+". Loading graph...",
                                      10000)

        y_adj = [c, self.x[0]*m+c, self.x[-1]*m+c]
        x_adj = [0, self.x[0], self.x[-1]]

        text_result = "f(x) = {0:.2}*x{1:+.2}".format(m, c)
        r2 = "R2 = {0:.2}".format(r)

        plot = pygal.XY(stroke=True, style=PlotStyle, disable_xml_declaration=True)
        plot.title = os.path.basename(datafile)
        plot.x_title = 'Shear rate'
        plot.y_title = 'Shear stress'
        plot.legend_at_bottom = True
        plot.config.css.append('../css/base-new.css')

        plot.add('Experimental data', [(x, y) for x, y in zip(self.x, self.y)])
        plot.add('Fit {0} ({1})'.format(text_result, r2), [(x, y) for x, y in zip(x_adj, y_adj)])
        plot.add('Used data', [(x, y) for x, y in zip(self.x[i:i+step], self.y[i:i+step])])
        plot_html = plot.render()

        page_html = "<!DOCTYPE html><html><head><script type=\"text/javascript\" src=\"http://kozea.github.com/pygal.js/javascripts/svg.jquery.js\"></script><script type=\"text/javascript\" src=\"http://kozea.github.com/pygal.js/javascripts/pygal-tooltips.js\"></script></head><body>"\
                    ""+plot_html+""\
                    "</body></html>"

        self.ui.plot_webview.setContent(page_html)
        self.ui.statusbar.showMessage("Graph loaded.", 5000)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    gui = Main()
    gui.show()
    sys.exit(app.exec_())