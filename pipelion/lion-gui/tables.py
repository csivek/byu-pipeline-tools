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

class TableItemType():
    Label = 0
    Button = 1

class TableEntry():
    def __init__(self, data):
        self.data = data
        self.createWidget(self.data)

    def createWidget(self, data):
        if data["type"] == TableItemType().Label:
            self.widget = TableLabel(data)
        elif self.data["type"] == TableItemType().Button:
            self.widget = TableButton(data)
        else:
            self.widget = TableLabel({"label":"BROKEN_DATA"})

    def updateData(self, data):
        if data["type"] != self.data["type"]:
            self.createWidget(data)
        self.data = data
        self.widget.setData(data)
        self.widget.update()

class TableLabel(QtWidgets.QLabel):
    def __init__(self, label, data):
        super(TableMultiLabel, self).__init__("")
        setData(data)

    def setData(self, data):
        self.setText(data["label"])

class TableButton(QtWidgets.QPushButton):
    def __init__(self, data):
        super(TableMultiLabel, self).__init__()
        setData(data)

    def setData(self, data):
        self.setText(data["label"])
        if "action" in data:
            self.clicked.connect(data["action"])

class TableModel():
    def __init__(self, entryData, headers):
        self.entries = {}
        for row in entryData:
            row = []
            for column in row:
                row.append(TableEntry(column))
            self.entries
        self.entries = entries
        self.headers = headers

    def itemAtIndex(self, row, column):
        return self.entries[row][column]

    def widgetAtIndex(self, row, column):
        return self.itemAtIndex(row, column).widget

    def updateSlotAtIndex(self, row, column):
        return self.widgetAtIndex(row, column).updateData

    def rows(self):
        return self.entries.keys()

    def rowCount(self):
        return len(self.entries.keys())

    def columns(self, key):
        return self.entries[key]

    def columnCount(self):
        if len(self.entries) > 0:
            return len(self.entries[self.entries.keys()[0]])
        else:
            return 0

class Table(QtWidgets.QTableWidget):
    def __init__(self, tableModel):
        super(Table, self).__init__()
        self.setModel(tableModel)
        # enable sorting
        #self.setSortingEnabled(True)

    def setModel(self, model):
        self.setRowCount(model.rowCount())
        self.setColumnCount(model.columnCount())
        self.verticalHeader().setVisible(False)
        self.setHorizontalHeaderLabels(model.headers)

        y = 0
        for row in model.rows():
            x = 0
            for column in model.columns(row):
                self.setCellWidget(x, y, model.widgetAtIndex(row, x))
                x += 1
            y += 1
        self.resizeColumnsToContents()
