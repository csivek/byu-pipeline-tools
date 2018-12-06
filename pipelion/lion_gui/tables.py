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
    def __init__(self, data):
        super(TableLabel, self).__init__("")
        self.setData(data)

    def setData(self, data):
        self.setText(data["label"])

class TableButton(QtWidgets.QPushButton):
    def __init__(self, data):
        super(TableButton, self).__init__()
        self.setData(data)

    def setData(self, data):
        self.setText(data["label"])
        if "action" in data:
            self.clicked.connect(data["action"])

class TableModel():
    def __init__(self, entryData, headers):
        print("\n\n\nTABLE MODEL\n\n\n")
        print(entryData)
        self.entries = []
        for row in entryData.keys():
            entry = []
            for column in entryData[row]:
                entry.append(TableEntry(column))
            self.entries.append(entry)
        self.headers = headers

    def entryAtIndex(self, row, column):
        return self.entries[row][column]

    def widgetAtIndex(self, row, column):
        return self.entryAtIndex(row, column).widget

    def updateSlotAtIndex(self, row, column):
        return self.widgetAtIndex(row, column).updateData

    def rowCount(self):
        return len(self.entries)

    def columnCount(self):
        if len(self.entries) > 0:
            return len(self.entries[0])
        else:
            return 0

class Table(QtWidgets.QTableWidget):
    def __init__(self, tableModel):
        super(Table, self).__init__()
        self.setModel(tableModel)
        # enable sorting
        #self.setSortingEnabled(True)

    def setModel(self, model):
        self.model = model
        self.setRowCount(self.model.rowCount())
        self.setColumnCount(self.model.columnCount())
        self.verticalHeader().setVisible(False)
        self.setHorizontalHeaderLabels(self.model.headers)

        for y in range(self.model.rowCount()):
            for x in range(self.model.columnCount()):
                print(self.model.entryAtIndex(y, x).data)
                self.setCellWidget(y, x, self.model.widgetAtIndex(y, x))

        self.resizeColumnsToContents()
