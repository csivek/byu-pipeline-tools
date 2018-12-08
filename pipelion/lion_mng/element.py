
from .files import *



class Element:
	def __init__(self, dept):
		self.dept = dept
		self.user = None
		self.steps = {"created":0,} #steps come from config.lion
	def assignUser(self, user):
		self.user = user
	def getUser(self):
		return self.user
	def getDept(self):
		return self.dept
	def setStep(self, name, value):
		self.steps[name] = value
	def getSteps(self):
		return self.steps
	def toJson(self):
		json = {}
		json['dept'] = self.dept
		json['user'] = self.user
		json['steps'] = self.steps
		return json
	def writeSelfToFile(self, parentBody):
		from .reader import ProductionRoot
		element_home_dir = ProductionRoot() + "/" + parentBody.getFilePath() + "/" + self.dept
		create_directory(element_home_dir)
		write_file(element_home_dir, "/element.json", self.toJson())
	def prettyPrint(self, level=1):
		indent = "".join(["\t"]*level)
		print(indent + "{")
		print(indent + "\tDEPT: " + self.dept)
		print(indent + "\tUSER: " + str(self.user) )
		print(indent + "\tSTEPS: [")
		for step in self.steps:
			print(indent + "\t\t" + step + ": " + str(self.steps[step]))
		print(indent + "\t]")
		print(indent + "}")
