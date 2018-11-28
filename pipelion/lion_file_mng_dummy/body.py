
from .element import Element
from .history import History
import time


class Body:
	def __init__(self, path, depts, user):
		'''
		creates a Body instance describing the asset or shot stored in the given filepath
		'''
		self._path = path
		elems = []
		for dept in depts:
			elems.append(Element(dept))
		self._elements = elems
		self._history = [History("body","CREATe", time.time(), user, "Created asset")]
	def addElement(self, dept):
		self._elements.append(Element(dept))
		# TODO: createElementDirectory(dept)
	def removeElement(self, dept):
		# TODO: deleteElementDirectory(dept)
		pass
	def getElement(self, dept):
		for elem in self._elements:
			if elem.getDept() == dept:
				return elem
		return None
	def prettyPrint(self, level):
		indent = "".join(["\t"]*level)
		print(indent + "{")
		print(indent + "\tPATH: " + self._path)
		print(indent + "\tELEMENTS: [" )
		for elem in self._elements:
			elem.prettyPrint(level + 2)
		print(indent + "\t]")
		print(indent + "\tHISTORY: [")
		for hist in self._history:
			hist.prettyPrint(level + 2)
		print(indent + "\t]")
		print(indent + "}")
