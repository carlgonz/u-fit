#!/bin/sh
pyuic4 mainwindow.ui -o ../python/forms/MainWindow_UI.py
pyuic4 about.ui -o ../python/forms/About_UI.py
pyuic4 about_alges.ui -o ../python/forms/AboutAlges_UI.py

#pyrcc4 logos.qrc -o ../python/forms/logos_rc.py


