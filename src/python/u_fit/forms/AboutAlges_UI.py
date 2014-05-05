# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_alges.ui'
#
# Created: Mon May  5 17:36:16 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutAlgesWidget(object):
    def setupUi(self, AboutAlgesWidget):
        AboutAlgesWidget.setObjectName(_fromUtf8("AboutAlgesWidget"))
        AboutAlgesWidget.resize(500, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutAlgesWidget.sizePolicy().hasHeightForWidth())
        AboutAlgesWidget.setSizePolicy(sizePolicy)
        AboutAlgesWidget.setMaximumSize(QtCore.QSize(500, 350))
        AboutAlgesWidget.setWindowTitle(QtGui.QApplication.translate("AboutAlgesWidget", "About ALGES", None, QtGui.QApplication.UnicodeUTF8))
        AboutAlgesWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtGui.QVBoxLayout(AboutAlgesWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelIcon = QtGui.QLabel(AboutAlgesWidget)
        self.labelIcon.setMaximumSize(QtCore.QSize(16777215, 100))
        self.labelIcon.setStyleSheet(_fromUtf8("background-color: rgb(84, 98, 122);"))
        self.labelIcon.setText(QtGui.QApplication.translate("AboutAlgesWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/&lt;no prefix&gt;/images/logo_alges_w.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIcon.setTextFormat(QtCore.Qt.AutoText)
        self.labelIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIcon.setObjectName(_fromUtf8("labelIcon"))
        self.verticalLayout.addWidget(self.labelIcon)
        self.label = QtGui.QLabel(AboutAlgesWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label.setText(QtGui.QApplication.translate("AboutAlgesWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Advanced Laboratory for </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Geostatistical Supercomputing</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.alges.cl\"><span style=\" text-decoration: underline; color:#004190;\">www.alges.cl</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(AboutAlgesWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutAlgesWidget)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutAlgesWidget.close)
        QtCore.QMetaObject.connectSlotsByName(AboutAlgesWidget)

    def retranslateUi(self, AboutAlgesWidget):
        pass

from u_fit import logos_rc
