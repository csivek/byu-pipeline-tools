import sys
import os
import threading
import traceback

try:
    from PySide import QtGui as QtGui
    from PySide.QtCore import Qt, Slot, Signal, QObject
except ImportError:
    from PySide2 import QtGui
    from PySide2.QtCore import Qt, Slot, Signal, QObject

from tables import *
import pipelion.lion_mng.reader as Reader
from pipelion.lion_mng.logger import Logger
from resources import *
from dialogs import *

class ViewModelSignals(QObject):
    updateProduction = Signal(str)
    updateDepartment = Signal(str)
    updateBody = Signal(str)

this = sys.modules[__name__]

def initialize():
    this.signals = ViewModelSignals()

    this.loggerEvent = threading.Event()
    this.logger = Logger(this.loggerEvent)
    this.logger.start()
    this.logger.productionUpdate.connect(this.productionUpdate, Qt.QueuedConnection)
    #QtGui.QGuiApplication.lastWindowClosed.connect(this.endLoggerThread)
    this.userBodies = Reader.getBodiesByUser()
    this.allBodies = Reader.getBodies()

@Slot()
def endLoggerThread():
    this.loggerEvent.set()

@Slot(str)
def productionUpdate(update):
    print("Production update in viewmodel: " + update)
    this.userBodies = Reader.getBodiesByUser()
    this.allBodies = Reader.getBodies()
    this.signals.updateProduction.emit(update)
    this.signals.updateDepartment.emit(update)
    this.signals.updateBody.emit(update)

def printThings():
    print("Things")

def checkedOutButtons():
    buttons = []
    buttons.append(TableData.buttonEntry(Strings.open, Styles().openButton, Styles().disabledButton, this.printThings))
    buttons.append(TableData.buttonEntry(Strings.sync, Styles().syncButton, Styles().disabledButton, this.printThings))
    buttons.append(None)
    buttons.append(TableData.buttonEntry(Strings.delete, Styles().deleteButton, Styles().disabledButton, this.printThings))
    return buttons

def checkedOutTable():
    entries = []
    for body in this.userBodies:
        departments = ", ".join(elem.dept for elem in body.getDepartments())
        entry = (body.path, body.type[1], departments, body.getDirectorySize())
        print(entry)
        entries.append(entry)
    headers = []
    headers.append(TableData.labelHeader(Strings.path, resizeMode=QtWidgets.QHeaderView.Interactive))
    headers.append(TableData.labelHeader(Strings.type, resizeMode=QtWidgets.QHeaderView.ResizeToContents))
    headers.append(TableData.labelHeader(Strings.departments))
    headers.append(TableData.labelHeader(Strings.size, resizeMode=QtWidgets.QHeaderView.ResizeToContents))
    return entries, headers


def bodyOverviewTable(bodyType):
    bodies = [body for body in this.allBodies if body.type[0] == bodyType[0]]
    entries = []
    for body in bodies:
        departments = ", ".join(elem.dept for elem in body.getDepartments())
        entries.append((body.path, departments))
    headers = []
    headers.append(TableData.labelHeader(Strings.path, resizeMode=QtWidgets.QHeaderView.Interactive))
    headers.append(TableData.labelHeader(Strings.departments, resizeMode=QtWidgets.QHeaderView.Stretch))
    return entries, headers


def departmentTable():
    tableData = {}
