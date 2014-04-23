__author__ = 'cgonzalez'

import os
import numpy as np
import pygal
from pygal.style import RedBlueStyle as PlotStyle

from PyQt4 import QtGui
from PyQt4 import QtCore

from .modules import regression
from .forms.MainWindow_UI import *
from .forms.AboutAlges_UI import *
from .forms.About_UI import *


class Main(QtGui.QMainWindow):
    def __init__(self):
        """
        Main window initialization
        """

        QtGui.QMainWindow.__init__(self)

        #Instance variables
        self.x = []
        self.y = []
        self.datafile = ""

        #UI settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Signals
        self.ui.update_button.clicked.connect(self.manualupdate_plot)
        self.ui.datafile_button.clicked.connect(self.select_file)
        self.ui.about_action.triggered.connect(self.show_about)
        self.ui.aboutalges_action.triggered.connect(self.show_about_alges)

        self.ui.datasize_spinbox.valueChanged.connect(self.autoupdate_plot)
        self.ui.alpha_spinbox.valueChanged.connect(self.autoupdate_plot)
        self.ui.datasize_check.toggled.connect(self.autoupdate_plot)

        self.ui.alpha_spinbox.valueChanged.connect(lambda x: self.ui.alpha_slider.setValue(int(x*1000)))
        self.ui.alpha_slider.valueChanged.connect(lambda x: self.ui.alpha_spinbox.setValue(float(x/1000)))


    def select_file(self):
        """
        Opens file dialog
        """
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open datafile",
                                                     QtCore.QDir.currentPath(),
                                                     "Text files (*.txt);"
                                                     "Comma separated (*.csv);"
                                                     "All files (*.*)")

        self.ui.datafile_line.setText(filename)

        self.datafile = self.ui.datafile_line.text()
        self.load_data(self.datafile)

        self.autoupdate_plot(0)

    def load_data(self, filename, cls=(1, 2)):
        """
        Loads data from file
        """
        try:
            data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=cls)
            self.x = data[:, 0]
            self.y = data[:, 1]
        except FileNotFoundError:
            self.x = []
            self.y = []
            self.ui.statusbar.showMessage("File not found.", 5000)

    def adjust(self):
        """
        Performs lineal regression.
        Returns:
        m - Slope or gradient
        c - Intercept
        r - Correlation coefficient
        i - Index of sub-sample first element
        len - Lenght of sub-sample
        """
        reg = regression.Regression(self.x, self.y)
        percentil = self.ui.datasize_spinbox.value()
        return reg.regression(percentil)

    def optimal_fit(self):
        """
        Performs the optimal lineal regression.
        Returns:
        m - Slope or gradient
        c - Intercept
        r - Correlation coefficient
        i - Index of sub-sample first element
        len - Lenght of sub-sample
        """
        reg = regression.Regression(self.x, self.y)
        slc = list(range(5, 60, 2))
        alp = self.ui.alpha_spinbox.value()
        i_op, f_op, m_op, c_op, r_op = reg.optimization(alpha=alp, steps=slc)
        return m_op, c_op, r_op, i_op, f_op


    def autoupdate_plot(self, value):
        """
        Auto update plot slot
        """
        if self.ui.autoupdate_check.isChecked():
            self.update_plot()

    def manualupdate_plot(self):

        if self.datafile != self.ui.datafile_line.text():
            self.datafile = self.ui.datafile_line.text()
            self.load_data(self.datafile)

        self.update_plot()

    def update_plot(self):
        """
        Main function, load data, perform adjust and show plot
        """
        if (len(self.x) == 0) or (len(self.y) == 0):
            return

        try:
            if self.ui.datasize_check.isChecked():
                [m, c, r, i, step] = self.adjust()
            else:
                [m, c, r, i, step] = self.optimal_fit()

        except Exception as e:
            self.ui.statusbar.showMessage("Error, please try again.", 2000)
            print(e)
            return

        y_adj = [c, self.x[0]*m+c, self.x[-1]*m+c]
        x_adj = [0, self.x[0], self.x[-1]]

        str_fx = "f(x) = {0:.2}*x{1:+.2}".format(m, c)
        str_r2 = "R2 = {0:.4}".format(r)
        str_fit = "{0} ({1})".format(str_fx, str_r2)

        plot = pygal.XY(stroke=True, style=PlotStyle, disable_xml_declaration=True)
        plot.title = os.path.basename(self.datafile)
        plot.x_title = 'Shear rate'
        plot.y_title = 'Shear stress'
        plot.legend_at_bottom = True
        css_dir = os.path.split(__file__)[0].replace('python', 'css')
        plot.config.css.append(css_dir+'/base-new.css')

        plot.add('Experimental data', [(x, y) for x, y in zip(self.x, self.y)])
        plot.add('Fit {0}'.format(str_fit), [(x, y) for x, y in zip(x_adj, y_adj)])
        # plot.add('Used data', [(x, y) for x, y in zip(self.x[i:i+step], self.y[i:i+step])])
        plot_html = plot.render()

        page_html = self.__get_page(plot_html)

        self.ui.plot_webview.setContent(page_html)
        self.ui.statusbar.showMessage("Graph loaded.", 5000)

    def __get_page(self, body):
        """
        Returns full html with given body
        """
        # js_dir = "http://kozea.github.com/pygal.js/javascripts"
        js_dir = "file://"+os.path.split(__file__)[0].replace('python', 'js')
        js1 = js_dir+"/svg.jquery.js"
        js2 = js_dir+"/pygal-tooltips.js"

        page_html = "<!DOCTYPE html><html><head>" \
                    "<script src=\""+js1+"\"></script>" \
                    "<script src=\""+js2+"\"></script>" \
                    "</head><body>"+body+"</body></html>"

        return page_html

    def show_about(self):
        #Display about alges dialog
        widget = AboutWindow(self)
        widget.show()

    def show_about_alges(self):
        #Display about dialog
        widget = AboutAlgesWindow(self)
        widget.show()


class AboutAlgesWindow(QtGui.QDialog):
    """
    About dialog for ALGES
    """
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AboutAlgesWidget()
        self.ui.setupUi(self)


class AboutWindow(QtGui.QDialog):
    """
    About dialog for application
    """
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_AboutWidget()
        self.ui.setupUi(self)