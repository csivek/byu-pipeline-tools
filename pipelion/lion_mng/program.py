import os
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
		print("ARGS " + str(args))
		launchScriptLoc = self.launchScript
		if self.launchScript[0] != "/":
			launchScriptLoc = Directories.toolsDir() + "/" + self.launchScript
		my_env = os.environ.copy()
		my_env["LD_LIBRARY_PATH"] = ""
		command = [launchScriptLoc]
		for arg in args:
			command.append(arg)
		print("COMMANDS " + str(command))
		subprocess.Popen(command, env=my_env)
		#subprocess.call("python3 launchHoudini.py", shell=True)
		#pid = subprocess.Popen(args=["gnome-terminal", "--command=" + launchScriptLoc]).pid
		#print pid
		#subprocess.call(launchScriptLoc)
		#subprocess.call(["cd ~/pipelion/byu-pipeline-tools" + ";" + launchScriptLoc + "\ngnome-terminal -e"], stdout=subprocess.PIPE)
		#os.system("gnome-terminal \'" + launchScriptLoc + "\'")
		#output = subprocess.check_output([launchScriptLoc], creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP, cwd=os.path.dirname(os.path.realpath(__file__)))
		#print subprocess.check_call([launchScriptLoc])
		#subprocess.Popen(os.path.dirname(os.path.realpath(__file__)) + " | echo $LD_LIBRARY_PATH| pwd | " + launchScriptLoc, shell=True, stdout=subprocess.PIPE).stdout.read()
