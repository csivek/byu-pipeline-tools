import os
import json
from .element import Element
from .history import History
from .files import *
from .logger import Logger
import time



class Body:

	def __init__(self, root, type, path):
		'''
		either fills the Body with the data at the given location, or initalizes an empty one
		'''
		self.root = root
		self.type = type
		self.path = path
		#check if the json is there and read it in
		try:
			self.fillSelfFromJson()
		#coudln't read the json, initalize an empty self instead
		except:
			print("caught an exception")
			self.history = [History("body", "CREATE", time.time(), os.environ["USER"], "Initialized an empty body for " + self.path)]
			self.elements = {}
			self.writeSelfToFile()
			Logger.logUpdate()


	def initializeDepartments(self, depts):
		for dept in depts:
			self.addDepartment(dept)
		Logger.logUpdate()

	def addHistory(self, history):
		self.history.append(history)
		self.writeSelfToFile()

	def addDepartment(self, dept):
		elem = dept
		if (not isinstance(elem, Element)):
			elem = Element(dept) #dept was just a string, make an Element object
		if elem.dept in self.elements:
			return
		self.elements[elem.dept] = elem
		element_dir = self.getMyLocation() + "/" + elem.dept
		create_directory(element_dir)
		hist = History("body", "ADD DEPARTMENT", time.time(), os.environ["USER"], "Added " + elem.dept + " department")
		self.history.append(hist)
		self.writeSelfToFile()

	def assignUserToDepartment(self, user, dept):
		self.elements[dept].assignUser(user)
		self.writeSelfToFile()
		Logger.logUpdate()

	def removeDepartment(self, dept):
		dept_dir = self.getMyLocation() + "/" + dept
		delete_directory(dept_dir)
		del self.elements[dept]
		self.writeSelfToFile()

	def getDepartment(self, dept):
		return self.elements[dept]

	def getDepartments(self):
		depts = []
		for dept in self.elements:
			depts.append(self.elements[dept])
		return depts

	#overwrites my own data with the json data
	def fillSelfFromJson(self):
		other = readJsonSelf()
		self.history = other.history
		self.elements = other.elements

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

	def readJsonSelf():
		other = {}
		jsonSelf = read_file(self.getMyLocation(), "/body.json")
		other.history = []
		for histJson in jsonSelf['history']:
			other.history.append(History(histJson['dept'], histJson['type'], histJson['time'], histJson['user'], histJson['message']))
		other.elements = {}
		for elemJson in jsonSelf['elements']:
			elem = Element(elemJson['dept'], elemJson['program'])
			other.steps = elemJson['steps']
			other.user = elemJson['user']
			other.elements[elem.dept] = elem
		return other

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
