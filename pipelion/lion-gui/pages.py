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

class PageWidget(QtWidgets.QWidget):
    def __init__(self, pageLabel, pageLayout, isNestedPage=False):
        super(PageWidget, self).__init__()
        self.pageLabel = pageLabel
        self.isNestedPage = isNestedPage
        self.setLayout(pageLayout)

class DashboardPage(PageWidget):
    def __init__(self):
        self.pageLabel = "Dashboard"
        self.pageLayout = self.layoutPage()
        super(DashboardPage, self).__init__(self.pageLabel, self.pageLayout)

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is the dashboard page"))
        return pageLayout

class SettingsPage(PageWidget):
    def __init__(self):
        self.pageLabel = "Settings"
        self.pageLayout = self.layoutPage()
        super(SettingsPage, self).__init__(self.pageLabel, self.pageLayout)

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is the settings page"))
        return pageLayout

class AdminToolsPage(PageWidget):
    def __init__(self):
        self.pageLabel = "Admin Tools"
        self.pageLayout = self.layoutPage()
        super(AdminToolsPage, self).__init__(self.pageLabel, self.pageLayout)

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is the admin tools page"))
        return pageLayout

class BodyOverviewPage(PageWidget):
    def __init__(self, bodyType):
        self.bodyType = bodyType
        self.pageLabel = PipelionResources().BodyTypeNiceName(self.bodyType)
        self.pageLayout = self.layoutPage()
        super(BodyOverviewPage, self).__init__(self.pageLabel, self.pageLayout)

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is a body overview page for " + self.pageLabel))
        return pageLayout

class DepartmentPage(PageWidget):
    def __init__(self, department):
        self.department = department
        self.pageLabel = PipelionResources().DepartmentNiceName(self.department)
        self.pageLayout = self.layoutPage()
        super(DepartmentPage, self).__init__(self.pageLabel, self.pageLayout, isNestedPage=True)

    def layoutPage(self):
        pageLayout = QtWidgets.QHBoxLayout()
        pageLayout.addWidget(QtWidgets.QLabel("This is a department page for " + self.pageLabel))
        return pageLayout
