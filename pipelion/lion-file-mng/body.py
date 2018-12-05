
from .element import Element
from .history import History
import time


class Body:
	def __init__(self, type, path, depts, user):
		'''
		creates a Body instance describing the asset or shot stored in the given filepath
		'''
		self.type = type
		self.path = path
		elems = []
		for dept in depts:
			elems.append(Element(dept))
		self.elements = elems
		self.history = [History("body","CREATe", time.time(), user, "Created asset")]
	def addElement(self, dept):
		self.elements.append(Element(dept))
		# TODO: createElementDirectory(dept)
		# create_asset() takes the body object and writes it to the right place
	def removeElement(self, dept):
		# TODO: deleteElementDirectory(dept)
		pass
	def getElement(self, dept):
		for elem in self.elements:
			if elem.getDept() == dept:
				return elem
		return None
	def prettyPrint(self, level):
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
