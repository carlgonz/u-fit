#!/bin/sh
pyuic4 mainwindow.ui -o ../python/u_fit/forms/MainWindow_UI.py
pyuic4 about.ui -o ../python/u_fit/forms/About_UI.py
pyuic4 about_alges.ui -o ../python/u_fit/forms/AboutAlges_UI.py

#pyrcc4 logos.qrc -o ../python/forms/logos_rc.py


