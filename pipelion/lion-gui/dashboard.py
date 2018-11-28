#!/usr/bin/python

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

import json

class Pipelion:
	def __init__(self):
		self.importLionFiles()

	def importLionFiles(self):
		# Import config.lion
		self.config = json.loads(open("../config.lion").read())

		# Import show name, icon, etc
		self.show = self.config["show"]
		print("Show Name: " + self.show["name"])

		# Import a list of programs used in this show
		self.programs = {}
		print("Importing program list...")
		for program in self.config["programs"]:
			print(program["name"])
			self.programs[program["id"]] = program

		# Import a list of deparments in this show
		self.departments = {}
		print("Importing department list...")
		for department in self.config["departments"]:
			print(department["name"])
			self.departments[department["id"]] = department

		# Import settings.lion
		self.settings = json.loads(open("../settings.lion").read())

	def startProgram(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.main_window = MainWindow(self)
		self.main_window.show()
		self.app.exec_()

class ProgramButton(QtWidgets.QPushButton):
    def __init__(self, pipelion, program):
        self.pipelion = pipelion
        self.program = program
        icon = QtWidgets.QIcon("../" + program["icon"])
        title = program["name"]
        super(ProgramButton, self).__init__(icon, title)

class ProgramBar(QtWidgets.QButtonGroup):
    def __init__(self, pipelion, main_window, program_buttons):
        self.pipelion = pipelion
        self.main_window = main_window
        super(ProgramBar, self).__init__()
        for program_button in program_buttons:
            self.addButton(program_button)
        self.buttonClicked[int].connect(lambda x: self.handle(x))

    @Slot(int)
    def handle(self, index):
        self.main_window.startProgram(self.button(index).program)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pipelion):
		self.pipelion = pipelion
		super(MainWindow, self).__init__()
		self.createPanes()
		self.setWindowTitle("Pipelion")

    def createPanes(self):
        self.createProgramBar()
        self.createCheckedOutPane()
        self.createMainPane()
        self.createPreviewPane()

    @Slot(int)
    def startProgram(self, index):
		print("called it")
		print(index)

    def startProgram(self, program, file="untitled"):
        print("Starting " + program["name"])
        print("Opening " + file + "." + program["extension"])

    def createProgramBar(self):
        programButtons = []
        for key in self.pipelion.programs.keys():
            program = self.pipelion.programs[key]
            programButtons.append(ProgramButton(self.pipelion, program))
        programBar = ProgramBar(self.pipelion, self, programButtons)
        dockable = QtWidgets.QDockWidget("Programs", self)
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        for programButton in programButtons:
            layout.addWidget(programButton)
        container.setLayout(layout)
        dockable.setWidget(container)
        dockable.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, dockable)

    def createCheckedOutPane(self):
        items = QtWidgets.QDockWidget("Checked Out", self)
        listWidget = QtWidgets.QListWidget()
        listWidget.addItem("item1")
        items.setWidget(listWidget)
        items.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, items)

    def createMainPane(self):
        items = QtWidgets.QDockWidget("Main", self)
        listWidget = QtWidgets.QListWidget()
        listWidget.addItem("item1")
        items.setWidget(listWidget)
        items.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, items)

    def createPreviewPane(self):
        items = QtWidgets.QDockWidget("Preview", self)
        listWidget = QtWidgets.QListWidget()
        listWidget.addItem("item1")
        items.setWidget(listWidget)
        items.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, items)

pipelion = Pipelion()

pipelion.startProgram()
