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

class Dialogs():
    def showOpenBodyDialog(self, path):
        openDialog = OpenDialog(path)
        openDialog.show()
    def showOpenBodyDialog(self, path, dept):
        openDialog = OpenDialog(path, dept)
        openDialog.show()
    def showSyncBodyDialog(self, path):
        syncDialog = SyncDialog(path)
        syncDialog.show()
    def showDeleteCheckedOutBodyDialog(self, path):
        syncDialog = SyncDialog(path)
        syncDialog.show()

class OpenDialog(QtWidgets.QWidget):
    def __init__(self, path, dept=None):
        super(OpenDialog, self).__init__()
        self.path = path
        self.dept = dept

class SyncDialog(QtWidgets.QWidget):
    def __init__(self, path):
        super(SyncDialog, self).__init__()
        self.path = path
