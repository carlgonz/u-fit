# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Apr 23 18:47:44 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plot_layout = QtGui.QVBoxLayout()
        self.plot_layout.setObjectName(_fromUtf8("plot_layout"))
        self.plot_webview = QtWebKit.QWebView(self.centralwidget)
        self.plot_webview.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.plot_webview.setObjectName(_fromUtf8("plot_webview"))
        self.plot_layout.addWidget(self.plot_webview)
        self.gridLayout.addLayout(self.plot_layout, 0, 0, 1, 1)
        self.settings_layout = QtGui.QVBoxLayout()
        self.settings_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.settings_layout.setObjectName(_fromUtf8("settings_layout"))
        self.settings_group = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_group.sizePolicy().hasHeightForWidth())
        self.settings_group.setSizePolicy(sizePolicy)
        self.settings_group.setBaseSize(QtCore.QSize(300, 0))
        self.settings_group.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_group.setObjectName(_fromUtf8("settings_group"))
        self.gridLayout_2 = QtGui.QGridLayout(self.settings_group)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.alpha_slider = QtGui.QSlider(self.settings_group)
        self.alpha_slider.setMaximum(1000)
        self.alpha_slider.setSingleStep(5)
        self.alpha_slider.setOrientation(QtCore.Qt.Horizontal)
        self.alpha_slider.setObjectName(_fromUtf8("alpha_slider"))
        self.gridLayout_2.addWidget(self.alpha_slider, 2, 3, 1, 2)
        self.alpha_label = QtGui.QLabel(self.settings_group)
        self.alpha_label.setText(QtGui.QApplication.translate("MainWindow", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.alpha_label.setObjectName(_fromUtf8("alpha_label"))
        self.gridLayout_2.addWidget(self.alpha_label, 2, 1, 1, 1)
        self.alpha_spinbox = QtGui.QDoubleSpinBox(self.settings_group)
        self.alpha_spinbox.setDecimals(3)
        self.alpha_spinbox.setSingleStep(0.05)
        self.alpha_spinbox.setObjectName(_fromUtf8("alpha_spinbox"))
        self.gridLayout_2.addWidget(self.alpha_spinbox, 2, 2, 1, 1)
        self.datafile_button = QtGui.QPushButton(self.settings_group)
        self.datafile_button.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.datafile_button.setObjectName(_fromUtf8("datafile_button"))
        self.gridLayout_2.addWidget(self.datafile_button, 0, 4, 1, 1)
        self.datasize_slider = QtGui.QSlider(self.settings_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datasize_slider.sizePolicy().hasHeightForWidth())
        self.datasize_slider.setSizePolicy(sizePolicy)
        self.datasize_slider.setMinimum(0)
        self.datasize_slider.setMaximum(100)
        self.datasize_slider.setPageStep(5)
        self.datasize_slider.setProperty("value", 25)
        self.datasize_slider.setOrientation(QtCore.Qt.Horizontal)
        self.datasize_slider.setInvertedControls(False)
        self.datasize_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.datasize_slider.setTickInterval(10)
        self.datasize_slider.setObjectName(_fromUtf8("datasize_slider"))
        self.gridLayout_2.addWidget(self.datasize_slider, 4, 3, 1, 2)
        self.datafile_line = QtGui.QLineEdit(self.settings_group)
        self.datafile_line.setObjectName(_fromUtf8("datafile_line"))
        self.gridLayout_2.addWidget(self.datafile_line, 0, 2, 1, 2)
        self.datasize_spinbox = QtGui.QSpinBox(self.settings_group)
        self.datasize_spinbox.setSuffix(QtGui.QApplication.translate("MainWindow", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.datasize_spinbox.setMinimum(1)
        self.datasize_spinbox.setMaximum(100)
        self.datasize_spinbox.setProperty("value", 25)
        self.datasize_spinbox.setObjectName(_fromUtf8("datasize_spinbox"))
        self.gridLayout_2.addWidget(self.datasize_spinbox, 4, 2, 1, 1)
        self.datasize_check = QtGui.QCheckBox(self.settings_group)
        self.datasize_check.setText(QtGui.QApplication.translate("MainWindow", "Window", None, QtGui.QApplication.UnicodeUTF8))
        self.datasize_check.setChecked(True)
        self.datasize_check.setObjectName(_fromUtf8("datasize_check"))
        self.gridLayout_2.addWidget(self.datasize_check, 4, 0, 1, 2)
        self.datafile_label = QtGui.QLabel(self.settings_group)
        self.datafile_label.setText(QtGui.QApplication.translate("MainWindow", "Datafile", None, QtGui.QApplication.UnicodeUTF8))
        self.datafile_label.setAlignment(QtCore.Qt.AlignCenter)
        self.datafile_label.setObjectName(_fromUtf8("datafile_label"))
        self.gridLayout_2.addWidget(self.datafile_label, 0, 1, 1, 1)
        self.settings_layout.addWidget(self.settings_group)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.autoupdate_check = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoupdate_check.sizePolicy().hasHeightForWidth())
        self.autoupdate_check.setSizePolicy(sizePolicy)
        self.autoupdate_check.setText(QtGui.QApplication.translate("MainWindow", "Auto update", None, QtGui.QApplication.UnicodeUTF8))
        self.autoupdate_check.setChecked(True)
        self.autoupdate_check.setObjectName(_fromUtf8("autoupdate_check"))
        self.horizontalLayout.addWidget(self.autoupdate_check)
        self.update_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setMaximumSize(QtCore.QSize(130, 16777215))
        self.update_button.setBaseSize(QtCore.QSize(130, 0))
        self.update_button.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.horizontalLayout.addWidget(self.update_button)
        self.settings_layout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.settings_layout.addItem(spacerItem)
        self.gridLayout.addLayout(self.settings_layout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.file_menu = QtGui.QMenu(self.menubar)
        self.file_menu.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.file_menu.setObjectName(_fromUtf8("file_menu"))
        self.help_menu = QtGui.QMenu(self.menubar)
        self.help_menu.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.help_menu.setObjectName(_fromUtf8("help_menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.new_action = QtGui.QAction(MainWindow)
        self.new_action.setEnabled(False)
        self.new_action.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.new_action.setObjectName(_fromUtf8("new_action"))
        self.open_action = QtGui.QAction(MainWindow)
        self.open_action.setEnabled(False)
        self.open_action.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.open_action.setObjectName(_fromUtf8("open_action"))
        self.exit_action = QtGui.QAction(MainWindow)
        self.exit_action.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_action.setObjectName(_fromUtf8("exit_action"))
        self.about_action = QtGui.QAction(MainWindow)
        self.about_action.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.about_action.setObjectName(_fromUtf8("about_action"))
        self.aboutalges_action = QtGui.QAction(MainWindow)
        self.aboutalges_action.setText(QtGui.QApplication.translate("MainWindow", "About ALGES", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutalges_action.setObjectName(_fromUtf8("aboutalges_action"))
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.aboutalges_action)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())
        self.datafile_label.setBuddy(self.datafile_line)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exit_action, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.datafile_line, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.update_button.click)
        QtCore.QObject.connect(self.datasize_spinbox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.datasize_slider.setValue)
        QtCore.QObject.connect(self.datasize_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.datasize_spinbox.setValue)
        QtCore.QObject.connect(self.datasize_check, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.datasize_spinbox.setEnabled)
        QtCore.QObject.connect(self.datasize_check, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.datasize_slider.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.datafile_line, self.datafile_button)
        MainWindow.setTabOrder(self.datafile_button, self.alpha_spinbox)
        MainWindow.setTabOrder(self.alpha_spinbox, self.alpha_slider)
        MainWindow.setTabOrder(self.alpha_slider, self.datasize_check)
        MainWindow.setTabOrder(self.datasize_check, self.datasize_spinbox)
        MainWindow.setTabOrder(self.datasize_spinbox, self.datasize_slider)
        MainWindow.setTabOrder(self.datasize_slider, self.autoupdate_check)
        MainWindow.setTabOrder(self.autoupdate_check, self.update_button)
        MainWindow.setTabOrder(self.update_button, self.plot_webview)

    def retranslateUi(self, MainWindow):
        pass

from PyQt4 import QtWebKit
