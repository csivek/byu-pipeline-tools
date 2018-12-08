import os
from .element import Element
from .history import History
from .files import *
from .logger import Logger
import time


class Body:

	def __init__(self, type, path, depts):
		'''
		creates a Body instance describing the asset or shot stored in the given filepath
		'''
		self.type = type
		self.path = path
		self.elements = []
		for dept in depts:
			self.addElement(dept)
		self.history = [History("body","CREATE", time.time(), os.environ["USER"], "Created asset")]
	def addElement(self, dept):
		elem = Element(dept)
		self.elements.append(elem)
		elem.writeSelfToFile(self)
	def removeElement(self, dept):
		# TODO: deleteElementDirectory(dept)
		pass
	def getElement(self, dept):
		for elem in self.elements:
			if elem.getDept() == dept:
				return elem
		return None
	def getFilePath(self):
		return self.type[1].lower() + "/" + self.path.replace("/", "-")
	def getMyLocation(self):
		from .reader import ProductionRoot
		return ProductionRoot() + "/" + self.getFilePath()
	def writeSelfToFile(self):
		create_directory(self.getMyLocation())
		write_file(self.getMyLocation(), "/body.json", self.toJson())
	def selfDestruct(self):
		delete_directory(self.getMyLocation())
		Logger.logUpdate()
	def toJson(self):
		json = {}
		json['type'] = self.type[0]
		json['path'] = self.path
		json['elements'] = []
		for elem in self.elements:
			json['elements'].append(elem.toJson())
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
