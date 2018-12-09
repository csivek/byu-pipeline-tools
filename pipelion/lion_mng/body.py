import os
import json
from .element import Element
from .history import History
from .files import *
from .logger import Logger
import time


class Body:

	def __init__(self, root, type, path, depts=None):
		'''
		creates a Body instance describing the asset or shot stored in the given filepath
		if "depts" is specified, it creates directories for them
		'''
		self.root = root
		self.type = type
		self.path = path
		#TODO actually check if the json is there and read it in
		jsonSelf = read_file(self.getMyLocation(), "/body.json")
		print(jsonSelf)

	def initializeDepartments(self, depts):
		self.elements = {}
		for dept in depts:
			self.addDepartment(dept)
		self.history = [History("body","CREATE", time.time(), os.environ["USER"], "Created asset")]
		self.writeSelfToFile()
		Logger.logUpdate()

	def setRoot(self, newRoot):
		self.root = newRoot

	def addDepartment(self, dept):
		elem = dept
		if (not isinstance(elem, Element)):
			elem = Element(self, dept) #dept was just a string, make an Element object
		else:
			elem.parentBody = self #we already have an Element, just reset its parentBody
		self.elements[elem.dept] = elem
		element_dir = self.getMyLocation() + "/" + elem.dept
		create_directory(element_dir)

	def removeDepartment(self, dept):
		# TODO: deleteElementDirectory(dept)
		pass

	def getDepartment(self, dept):
		return self.elements[dept]

	def getDepartments(self):
		depts = []
		for dept in self.elements:
			depts.append(self.elements[dept])
		return depts

	def syncSelf(self):
		#look for extra steps in each element, extra elements added, extra items in History[]
		print("pulling in any file data I don't have")

	def getFilePath(self):
		return self.type[1].lower() + "/" + self.path.replace("/", "-")

	def getMyLocation(self):
		return self.root + "/" + self.getFilePath()

	def writeSelfToFile(self):
		create_directory(self.getMyLocation())
		write_file(self.getMyLocation(), "/body.json", self.toJson())
		write_file(self.getMyLocation(), "/mini.json", {
			"root": self.root,
			"type": self.type,
			"path": self.path
		})

	def selfDestruct(self):
		delete_directory(self.getMyLocation())
		Logger.logUpdate()

	def toJson(self):
		json = {}
		json['root'] = self.root
		json['type'] = self.type[0]
		json['path'] = self.path
		json['elements'] = []
		for dept in self.elements:
			json['elements'].append(self.elements[dept].toJson())
		json['history'] = []
		for hist in self.history:
			json['history'].append(hist.toJson())
		return json

	def prettyPrint(self, level=1):
		indent = "".join(["\t"]*level)
		print(indent + "{")
		print(indent + "\tPATH: " + self.path)
		print(indent + "\tELEMENTS: [" )
		for elem in self.elements:
			elem.prettyPrint(level + 2)
		print(indent + "\t]")
		print(indent + "\tHISTORY: [")
		for hist in self.history:
			hist.prettyPrint(level + 2)
		print(indent + "\t]")
		print(indent + "}")

	def getPrograms(self):
		return [x.program for x in self.elements if x.program]
