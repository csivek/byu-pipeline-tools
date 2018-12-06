import sys
import os
try:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui as QtGui
    from PySide import QtCore
    from PySide.QtCore import Slot
except ImportError:
    from PySide2 import QtWidgets, QtGui, QtCore
    from PySide2.QtCore import Slot

from app import *
from resources import *

def main():
    app = PipelionApp()

    from window import *
    from resources import *

    mainWindow = MainWindow()
    mainWidget = QtWidgets.QWidget()
    mainLayout = QtWidgets.QHBoxLayout()

    screenLayout = ScreenLayout()
    sideBarLayout = SideBarLayout(screenLayout)

    mainLayout.addLayout(sideBarLayout)
    mainLayout.addLayout(screenLayout)
    mainWidget.setLayout(mainLayout)
    mainWindow.setCentralWidget(mainWidget)
    mainWindow.initialSize(0.7)
    mainWindow.setWindowTitle(PipelionResources().appName() + " - " + PipelionResources().showTitle())
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
