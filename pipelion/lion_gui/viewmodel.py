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

def checkedOutTable():
    tableData = {}
    for body in this.userBodies:
        controller = CheckoutEntryController(body)
        row = []
        row.append(TableData.labelEntry(body.path))
        row.append(TableData.buttonEntry(Strings.open, Styles().openButton, controller.showOpenBodyDialog))
        newHistories = Reader.getNewHistories(body.path)
        if len(newHistories) > 0:
            row.append(TableData.buttonEntry(Strings.sync, Styles().syncButton, controller.showSyncBodyDialog))
        else:
            row.append(TableData.labelEntry(Strings.nochanges))
        row.append(TableData.buttonEntry(Strings.delete, Styles().deleteButton, controller.showDeleteBodyDialog))
        tableData[body.path] = row

    headers = []
    headers.append(TableData.labelHeader(Strings.items))
    headers.append(TableData.buttonHeader(Strings.open))
    headers.append(TableData.buttonHeader(Strings.sync))
    headers.append(TableData.buttonHeader(Strings.delete))
    return tableData, headers

def bodyOverviewTable(bodyType):
    bodies = [body for body in this.allBodies if body.type[0] == bodyType[0]]
    tableData = {}
    for body in bodies:
        row = []
        row.append(TableData.labelEntry(body.path))
        departmentsLabel = ""
        for elementkey in body.elements:
            departmentsLabel += body.elements[elementkey].dept + " "
        row.append(TableData.buttonEntry(Strings.rename, Styles.renameButton, lambda: Dialogs().showRenameBodyDialog(body.path)))
        tableData[body.path] = row

    headers = []
    headers.append(TableData.labelHeader(Strings.items))
    headers.append(TableData.buttonHeader(Strings.open))
    return tableData, headers

def departmentTable():
    tableData = {}
