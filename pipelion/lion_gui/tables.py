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
    DisabledStyle = "disabled_style"
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
    def buttonEntry(label, style, disabledStyle, action=None):
        entry = {}
        entry[TableData.WidgetType] = TableData.WidgetTypes.Button
        entry[TableData.Label] = label
        entry[TableData.Style] = style
        entry[TableData.DisabledStyle] = disabledStyle
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

    class Role:
        OpenButton = "openButton"
        SyncButton = "syncButton"
        DeleteButton = "deleteButton"

    def __init__(self, data):
        super(TableButton, self).__init__()
        self.setData(data)

    def setData(self, data):
        self.data = data
        self.setText(self.data[TableData.Label])
        self.setEnabledStyle(False)
        if TableData.Action in self.data:
            self.clicked.connect(self.data[TableData.Action])

    def setAction(self, newAction):
        self.clicked.disconnect(self.data[TableData.Action])
        self.data[TableData.Action] = newAction
        self.clicked.connect(self.data[TableData.Action])

    def setEnabledStyle(self, enabled):
        if enabled:
            self.setStyleSheet(self.data[TableData.Style])
            self.repaint()
        else:
            self.setStyleSheet(self.data[TableData.DisabledStyle])
            self.repaint()

        self.setEnabled(enabled)

class TableBar(QtWidgets.QLabel):
    def __init__(self, buttonEntries):
        super(TableBar, self).__init__()
        layout = QtWidgets.QHBoxLayout()
        self.tableButtons = []
        for buttonEntry in buttonEntries:
            if buttonEntry is not None:
                print (buttonEntry)
                tableButton = TableButton(buttonEntry)
                tableButton.setFixedHeight(20)
                tableButton.setEnabledStyle(False)
                self.tableButtons.append(tableButton)
                layout.addWidget(tableButton)
                print (tableButton)
            else:
                layout.addStretch()

        self.setFixedHeight(40)
        self.setStyleSheet(Styles.tableBar)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        self.setLayout(layout)

    def setTable(self, table):
        self.table = table
        self.table.itemSelectionChanged.connect(self.selectionChanged)

    @Slot()
    def selectionChanged(self):
        print(self.table.selectedRanges())
        rowCount = 0
        for range in self.table.selectedRanges():
            rowCount += range.rowCount()
        if (rowCount == 1):



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, entries, headers):
        #print("\n\n\nTABLE MODEL\n\n\n")
        #print(entryData)
        self.entries = entries
        self.headers = headers

    def rowCount(self):
        return len(self.entries)

    def columnCount(self):
        if len(self.entries) > 0:
            return len(self.entries[0])
        else:
            return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return str(self.entries[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))



class Table(QtWidgets.QTableWidget):
    def __init__(self, model):
        super(Table, self).__init__()
        self.model = model
        self.setRowCount(self.model.rowCount())
        self.setColumnCount(len(self.model.headers))
        self.verticalHeader().setVisible(False)

        self.setHorizontalHeaderLabels([header[TableData.Label] for header in self.model.headers])

        horizontalHeader = self.horizontalHeader()
        for i in range(len(self.model.headers)):
            horizontalHeader.setSectionResizeMode(i, self.model.headers[i][TableData.ResizeMode])

        self.setSortingEnabled(True)
        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                self.setItem(row,column,QtWidgets.QTableWidgetItem(str(self.model.entries[row][column])))

        self.resizeColumnsToContents()
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
