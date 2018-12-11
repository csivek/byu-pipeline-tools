import subprocess
from production import Directories

class Program:
	def __init__(self, id, name, extension, icon, launchScript):
		self.id = id
		self.name = name
		self.extension = extension
		self.icon = icon
		self.launchScript = launchScript

	def runProgram(self, args):
		print("Running " + str(self.name))
		launchScriptLoc = self.launchScript
		if self.launchScript[0] != "/":
			launchScriptLoc = Directories.toolsDir() + "/" + self.launchScript
		subprocess.call(launchScriptLoc, shell=True)
