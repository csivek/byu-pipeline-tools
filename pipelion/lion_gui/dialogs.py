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

class CheckoutEntryController():
    def __init__(self, parentWidget, body):
        self.parentWidget = parentWidget
        self.body = body

    #@Slot()
    def showOpenBodyDialog(self):
        print("started from the bottom now we here")
        openDialog = CheckoutOpenDialog(self.body._path)
        openDialog.exec_()

    #@Slot()
    def showSyncBodyDialog(self):
        syncDialog = CheckoutSyncDialog(self.body._path)
        syncDialog.exec_()

    #@Slot()
    def showDeleteBodyDialog(self):
        syncDialog = CheckoutSyncDialog(self.body._path)
        syncDialog.exec_()

class CheckoutOpenDialog(QtWidgets.QMessageBox):
    def __init__(self, path, dept=None):
        super(CheckoutOpenDialog, self).__init__()
        self.path = path
        self.dept = dept

class CheckoutSyncDialog(QtWidgets.QMessageBox):
    def __init__(self, path):
        super(CheckoutSyncDialog, self).__init__()
        self.path = path
