#!/usr/bin/python

import sys
import os
try:
	from PySide import QtGui as QtWidgets
	from PySide import QtGui as QtGui
	from PySide import QtCore
except ImportError:
	from PySide2 import QtWidgets, QtGui, QtCore

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
			self.programs[program["name"]] = program

		# Import a list of deparments in this show
		self.departments = {}
		print("Importing department list...")
		for department in self.config["departments"]:
			print(department["name"])
			self.departments[department["name"]] = department

		# Import settings.lion
		self.settings = json.loads(open("../settings.lion").read())


	def startProgram(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.main_window = MainWindow(self)
		self.main_window.show()
		self.app.exec_()

class ProgramButton(QtWidgets.QPushButton):
    def __init__(self, pipelion, name, action):
        self.pipelion = pipelion
        icon = QIcon(config["programs"][name]["icon"])
        title = config["programs"][name]["title"]
        super(ProgramButton, self).__init__(self, icon, title)
        self.clicked.connect(action)

class ProgramBar(QtWidgets.QHBoxLayout):
    def __init__(self, pipelion, program_buttons):
        self.pipelion = pipelion
        super(ProgramBar, self).__init__()
        for program_button in program_buttons:
            self.addWidget(program_button)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pipelion):
		self.pipelion = pipelion
		super(MainWindow, self).__init__()
		self.createPanes()
		self.setWindowTitle("Pipelion")

    def createPanes(self):
        self.createToolBar()
        self.createCheckedOutPane()
        self.createMainPane()
        self.createPreviewPane()

    def createToolBar(self):
        programButtons = []
        #for program in config["programs"]:
            #programButtons += ProgramButton(program, lambda: self.startProgram(program))
        toolbar = QtWidgets.QToolBar("My ToolBar") #ProgramBar()
        self.addToolBar(toolbar)

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
