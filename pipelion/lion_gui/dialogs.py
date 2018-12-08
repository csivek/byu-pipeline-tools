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
        print(user)
        conflicts = checkSyncConflictBody(self.body.path,user)
        print(conflicts)
        if len(conflicts) == 0:
            syncDialog = QtWidgets.QMessageBox()
            syncDialog.setText("Asset (" + self.body.path + ") has been synced.")
            syncDialog.exec_()
            return

        #syncDialog = CheckoutSyncDialog(self.body, conflicts)
        syncDialog = QtWidgets.QMessageBox()
        syncDialog.setText("There were conflicts with the following files:")
        syncDialog.setDetailedText(str(syncDialog.conflicts))
        syncDialog.addButton(QtWidgets.QPushButton("Match Production"), QtWidgets.ButtonRole.AcceptRole)
        syncDialog.addButton(QtWidgets.QPushButton("Merge"), QtWidgets.ButtonRole.AcceptRole)
        syncDialog.addButton(QtWidgets.QPushButton("Keep My Changes"), QtWidgets.ButtonRole.AcceptRole)
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
