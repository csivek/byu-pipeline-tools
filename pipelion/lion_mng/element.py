
from .files import *



class Element:
	def __init__(self, dept, program=None):
		self.dept = dept
		self.user = None
		self.steps = {"created":0,} #steps come from config.lion
		self.program = program
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
