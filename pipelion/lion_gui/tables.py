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
from resources import Styles

class TableData():
    # Data members that act as keys in a dictionary
    WidgetType = "widget_type"
    Label = "label"
    Style = "style"
    Action = "action"

    # Data members for labels
    ResizeMode = "resize_policy"

    class WidgetTypes():
        Label = 0
        Button = 1

    @staticmethod
    def labelEntry(label):
        entry = {}
        entry[TableData.WidgetType] = TableData.WidgetTypes.Label
        entry[TableData.Label] = label
        return entry

    @staticmethod
    def labelHeader(label, resizeMode=QtWidgets.QHeaderView.Stretch):
        header = {}
        header[TableData.Label] = label
        header[TableData.ResizeMode] = resizeMode
        return header

    @staticmethod
    def buttonEntry(label, style, action=None):
        entry = {}
        entry[TableData.WidgetType] = TableData.WidgetTypes.Button
        entry[TableData.Label] = label
        entry[TableData.Style] = style
        if action is not None:
            entry[TableData.Action] = action
        return entry

    @staticmethod
    def buttonHeader(label, resizeMode=QtWidgets.QHeaderView.Fixed):
        header = {}
        header[TableData.Label] = label
        header[TableData.ResizeMode] = resizeMode
        return header


class TableEntry():
    def __init__(self, data):
        self.data = data
        self.createWidget(self.data)

    def createWidget(self, data):
        if data[TableData.WidgetType] == TableData.WidgetTypes.Label:
            self.widget = TableLabel(data)
        elif self.data[TableData.WidgetType] == TableData.WidgetTypes.Button:
            self.widget = TableButton(data)
        else:
            self.widget = TableLabel({TableData.Label:Strings.broken_data})

    def updateData(self, data):
        if data[TableData.WidgetType] != self.data[TableData.WidgetType]:
            self.createWidget(data)
        self.data = data
        self.widget.setData(data)
        self.widget.update()

class TableLabel(QtWidgets.QLabel):
    def __init__(self, data):
        super(TableLabel, self).__init__("")
        self.setStyleSheet('''
            padding: 10; margin:20
        ''')
        self.setData(data)

    def setData(self, data):
        self.setText(data[TableData.Label])

class TableButton(QtWidgets.QPushButton):
    def __init__(self, data):
        super(TableButton, self).__init__()
        self.setData(data)

    def setData(self, data):
        self.data = data
        self.setText(self.data[TableData.Label])
        self.setStyleSheet(self.data[TableData.Style])
        if TableData.Action in self.data:
            self.clicked.connect(self.data[TableData.Action])

    def setAction(self, newAction):
        self.clicked.disconnect(self.data[TableData.Action])
        self.data[TableData.Action] = newAction
        self.clicked.connect(self.data[TableData.Action])

class TableBar(QtWidgets.QLabel):
    def __init__(self, buttonEntries):
        super(TableBar, self).__init__()
        layout = QtWidgets.QHBoxLayout()
        self.tableEntries = []
        for buttonEntry in buttonEntries:
            if buttonEntry is not None:
                print (buttonEntry)
                tableButton = TableButton(buttonEntry)
                tableButton.setFixedHeight(20)
                self.tableEntries.append(tableButton)
                layout.addWidget(tableButton)
                print (tableButton)
            else:
                layout.addStretch()

        self.setFixedHeight(40)
        self.setStyleSheet(Styles.tableBar)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        self.setLayout(layout)

    @Slot(str)
    def selected(self, path):
        print(path)


class TableModel():
    def __init__(self, entryData, headers):
        #print("\n\n\nTABLE MODEL\n\n\n")
        #print(entryData)
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
        self.setColumnCount(len(self.model.headers))
        self.verticalHeader().setVisible(False)

        #print self.model.headers
        headerLabels = [ x[TableData.Label] for x in self.model.headers]
        self.setHorizontalHeaderLabels(headerLabels)


        horizontalHeader = self.horizontalHeader()
        for i in range(len(self.model.headers)):
            horizontalHeader.setSectionResizeMode(i, self.model.headers[i][TableData.ResizeMode])

        self.horizontalHeader().setVisible(False)

        for y in range(self.model.rowCount()):
            for x in range(self.model.columnCount()):
                #print(self.model.entryAtIndex(y, x).data)
                self.setCellWidget(y, x, self.model.widgetAtIndex(y, x))

        self.resizeColumnsToContents()
