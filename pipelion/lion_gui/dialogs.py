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

from pipelion.lion_mng.reader import *

class CheckoutEntryController():
    def __init__(self, body):
        self.body = body

    #@Slot()
    def showOpenBodyDialog(self):
        print("started from the bottom now we here")
        openDialog = CheckoutOpenDialog(self.body.path)
        openDialog.exec_()

    #@Slot()
    def showSyncBodyDialog(self):
        user = os.environ["USER"]
        conflicts = checkSyncConflictBody(self.body.path,user)
        if len(conflicts) == 0:
            syncDialog = QMessageBox()
            syncDialog.setText("Asset (" + self.body.path + ") has been synced.")
            syncDialog.exec_()
            return

        syncDialog = CheckoutSyncDialog(self.body, conflicts)
        syncDialog.exec_()

    #@Slot()
    def showDeleteBodyDialog(self):
        syncDialog = CheckoutSyncDialog(self.body.path)
        syncDialog.exec_()

class CheckoutOpenDialog(QtWidgets.QMessageBox):
    def __init__(self, path, dept=None):
        super(CheckoutOpenDialog, self).__init__()
        self.path = path
        self.dept = dept

class CheckoutSyncDialog(QtWidgets.QMessageBox):
    def __init__(self, body, conflicts):
        super(CheckoutSyncDialog, self).__init__()
        self.body = body
        self.conflicts = conflicts
