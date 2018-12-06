import sys
import os
try:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui as QtGui
    from PySide import QtCore
    from PySide.QtCore import Slot, Signal, QObject
except ImportError:
    from PySide2 import QtWidgets, QtGui, QtCore
    from PySide2.QtCore import Slot, Signal, QObject

from resources import *
from pages import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    def initialSize(self, percentage):
        dw = QtWidgets.QDesktopWidget()
        mainScreenSize = dw.availableGeometry(dw.primaryScreen())
        x = mainScreenSize.width() * percentage
        y = mainScreenSize.height() * percentage
        self.resize(x,y)

class ScreenLayout(QtWidgets.QStackedLayout):
    def __init__(self):
        super(ScreenLayout, self).__init__()
        self.pages = []
        self.setPages()
        for page in self.pages:
            self.addWidget(page)

    def setPages(self):
        self.pages.append(DashboardPage())
        for bodyType in PipelionResources().bodyTypes():
            self.pages.append(BodyOverviewPage(bodyType))
            for department in PipelionResources().departments(bodyType):
                self.pages.append(DepartmentPage(department))
        self.pages.append(SettingsPage())
        if(PipelionResources().isAdmin()):
            self.pages.append(AdminToolsPage())


class SideBarLink(QtWidgets.QLabel):

    clicked = Signal(int)

    def __init__(self, page, index):
        self.page = page
        self.index = index
        super(SideBarLink, self).__init__(self.page.pageLabel)
        if self.page.isNestedPage:
            self.setObjectName("nested")

    def mousePressEvent(self, event):
        self.clicked.emit(self.index)

class SideBarLayout(QtWidgets.QVBoxLayout):
    def __init__(self, screenLayout):
        super(SideBarLayout, self).__init__()
        self.screenLayout = screenLayout
        self.links = []
        self.initialLayout()

    def initialLayout(self):
        self.setSpacing(0)
        self.addWidget(self.logoWidget(PipelionResources().logoSize()))
        count = 0
        for page in self.screenLayout.pages:
            linkWidget = SideBarLink(page, count)
            self.links.append(linkWidget)
            self.addWidget(linkWidget)
            linkWidget.clicked.connect(self.screenLayout.setCurrentIndex)
            count += 1
        self.addStretch()

    def logoWidget(self, size):
        logoImage = QtGui.QImage(PipelionResources().logo())
        logoWidget = QtWidgets.QLabel()
        logoWidget.setPixmap(QtGui.QPixmap.fromImage(logoImage).scaled(size,size))
        logoWidget.setObjectName("logo")
        return logoWidget
