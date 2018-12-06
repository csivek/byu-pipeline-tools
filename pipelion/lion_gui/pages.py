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

from resources import *
from tables import *
from viewmodel import *
from programWidget import ProgramShelfWidget
from pipelion.lion_file_mng import production_reader

class PageWidget(QtWidgets.QScrollArea):
    def __init__(self, pageLabel, isNestedPage=False):
        super(PageWidget, self).__init__()
        self.pageLabel = pageLabel
        self.isNestedPage = isNestedPage
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor("#c2cec7"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def headerWidget(self, label):
        banner = QtWidgets.QWidget()

        bannerText = QtWidgets.QLabel(label)
        bannerText.setAlignment(QtCore.Qt.AlignCenter)
        bannerLayout = QtWidgets.QHBoxLayout()
        bannerLayout.setMargin(0)
        bannerLayout.addWidget(bannerText)
        banner.setLayout(bannerLayout)

        banner.setStyleSheet('''
        background-color: #364441; padding: 10; font-size: 16px; color: white
        ''')
        banner.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        return banner

class DashboardPage(PageWidget):
    def __init__(self):
        super(DashboardPage, self).__init__(Strings.dashboard)
        self.setLayout(self.layoutPage())

    def layoutPage(self):
        pageLayout = QtWidgets.QVBoxLayout()
        pageLayout.addWidget(self.headerWidget(Strings.shortcuts))
        programs = production_reader.getPrograms()
    	self.programShelfWidget = ProgramShelfWidget(programs, 100, 14, shortcuts=True)
        pageLayout.addWidget(self.programShelfWidget)
        pageLayout.addWidget(self.headerWidget(Strings.checkedoutitems))
        tableData, headers = ViewModel(self).checkedOutTable()
        table = Table(TableModel(tableData, headers))
        pageLayout.addWidget(table)
        return pageLayout


class SettingsPage(PageWidget):
    def __init__(self):
        super(SettingsPage, self).__init__(Strings.settings)
        self.setLayout(self.layoutPage())

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is the settings page"))
        return pageLayout

class AdminToolsPage(PageWidget):
    def __init__(self):
        super(AdminToolsPage, self).__init__(Strings.admin_tools)
        self.setLayout(self.layoutPage())

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is the admin tools page"))
        return pageLayout

class BodyOverviewPage(PageWidget):
    def __init__(self, bodyType):
        self.bodyType = bodyType
        super(BodyOverviewPage, self).__init__(PipelionResources().BodyTypeNiceName(self.bodyType))
        self.setLayout(self.layoutPage())

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is a body overview page for " + self.pageLabel))
        return pageLayout

class DepartmentPage(PageWidget):
    def __init__(self, department):
        self.department = department
        super(DepartmentPage, self).__init__(PipelionResources().DepartmentNiceName(self.department), isNestedPage=True)
        self.setLayout(self.layoutPage())

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is a department page for " + self.pageLabel))
        return pageLayout
