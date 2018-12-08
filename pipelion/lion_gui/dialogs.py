import sys
import os
import traceback
try:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui as QtGui
    from PySide import QtCore
    from PySide.QtCore import Slot
except ImportError:
    from PySide2 import QtWidgets, QtGui, QtCore
    from PySide2.QtCore import Slot

from pipelion.lion_mng.reader import *
from programWidget import ProgramShelfWidget

class CheckoutEntryController():
    def __init__(self, body):
        self.body = body

    #@Slot()
    def showOpenBodyDialog(self):

        try:
            print("started from the bottom now we here")
            openDialog = MultiOpenDialog(self.body)
            openDialog.exec_()
        except Exception as e:
            print("This is an exception: ", e)
            traceback.print_exc()

    #@Slot()
    def showSyncBodyDialog(self):
        user = os.environ["USER"]
        print(user)
        conflicts = checkSyncConflictBody(self.body.path,user)
        print(conflicts)
        print("breakpoint -5")
        if len(conflicts) == 0:
            print("breakpoint -4")
            syncDialog = QtWidgets.QMessageBox()
            print("breakpoint -3")
            syncDialog.setText("Asset (" + self.body.path + ") has been synced.")
            print("breakpoint -2")
            syncDialog.exec_()
            return

        print("breakpoint -1")
        #syncDialog = CheckoutSyncDialog(self.body, conflicts)
        syncDialog = QtWidgets.QMessageBox()
        syncDialog.setText("There were conflicts with the following files:")
        syncDialog.setDetailedText(str(conflicts))
        syncDialog.addButton(QtWidgets.QPushButton("Match Production"), QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        syncDialog.addButton(QtWidgets.QPushButton("Merge"), QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        syncDialog.addButton(QtWidgets.QPushButton("Keep My Changes"), QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        syncDialog.exec_()

    #@Slot()
    def showDeleteBodyDialog(self):
        syncDialog = CheckoutSyncDialog(self.body.path)
        syncDialog.exec_()

class MultiOpenDialog(QtWidgets.QDialog):
    def __init__(self, body):
        super(MultiOpenDialog, self).__init__()
        self.body = body
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Choose a program to open with:"))
        self.programShelfWidget = ProgramShelfWidget(self.body.getPrograms(), 50, 14)
        layout.addWidget(self.programShelfWidget)
        self.programShelfWidget.selectedSet.connect(self.programSelected)

        hlayout = QtWidgets.QHBoxLayout()
        self.openButton = QtWidgets.QPushButton("Open")
        self.openButton.setEnabled(False)
        self.openButton.clicked.connect(self.accept)
        self.cancelButton = QtWidgets.QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.reject)
        hlayout.addWidget(self.openButton)
        hlayout.addWidget(self.cancelButton)

        layout.addLayout(hlayout)
        self.setLayout(layout)

        self.selectedProgram = None

    def programSelected(self, i):
        if i == -1:
            self.openButton.setEnabled(False)
        else:
            self.openButton.setEnabled(True)
            self.selectedProgram = self.programShelfWidget.programs[i]


class CheckoutSyncDialog(QtWidgets.QMessageBox):
    def __init__(self, body, conflicts):
        super(CheckoutSyncDialog, self).__init__()
        self.body = body
        self.conflicts = conflicts
