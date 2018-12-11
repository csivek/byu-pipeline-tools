
from .body import Body
from .element import Element
from .history import History
from .program import Program
from .production import Production
from .department import Department
from .files import *
import time
import random
import json



def ProductionRoot():
	return os.environ["BYU_PROJECT_DIR"] + "/production"

def UserRoot(user):
	return os.environ["BYU_PROJECT_DIR"] + "/users/" + user


def getBodiesByUser(user=None):
	"""
	gets all bodies associated with a user
	"""
	if not user:
		user = os.environ['USER']
	body_paths = get_all_body_summary_filepaths(UserRoot(user))
	bodies = []

	for path in body_paths:
		jsonObj = read_file(path)
		bodies.append(Body(jsonObj['root'], jsonObj['type'], jsonObj['path']))

	return bodies

def getBodyTypes():
	return [("asset","Asset"),("shot","Shot")]

def getBodies(dept = None):
	"""
	Returns the specified body and all sub bodies that are associated with the specified departments
	"""
	body_paths = get_all_body_summary_filepaths(ProductionRoot())
	bodies = []

	for path in body_paths:
		jsonObj = read_file(path)
		body = Body(jsonObj['root'], jsonObj['type'], jsonObj['path'])
		if dept == None or body.containsDepartment(dept):
			bodies.append(body)
	print("***************************************************************************")
	return bodies

def getNewHistories(path = "root", user = "current"):
	"""
	get all updates to an asset that
	"""
	if random.randint(0,1) == 0:
		return []
	return [History("model","CHECKOUT", time.time(), "csivek", "csivek checked out asset " + path),History("body","PUBLISH", time.time(), "csivek", "csived created asset " + path)]

def getPrograms():
	programs = []
	programs.append(Program("usd", "USDView", "usd", "icons/usd.png", "/opt/hfs.current/bin/usdview"))
	programs.append(Program("maya", "Maya", "mb", "icons/maya.png", "app-launch-scripts/project_maya.sh"))
	programs.append(Program("hou", "Houdini", "hip", "icons/hou.png", "app-launch-scripts/project_houdini.sh"))
	programs.append(Program("mari", "Mari", "mari", "icons/mari.png", "app-launch-scripts/project_mari.sh"))
	programs.append(Program("nuke", "Nuke", "nk", "icons/nuke.png", "app-launch-scripts/project_nuke.sh"))
	programs.append(Program("file", "Extra Files", "*", "icons/file.png", "app-launch-scripts/project_file.sh"))
	return programs

def getDepartments():
	depts = []
	depts.append(Department("concept","asset","Concept",["file"],["Rough Draft", "Final"]))
	depts.append(Department("model","asset","Model",["maya","hou"],["Rough Draft", "Final"]))
	depts.append(Department("rig","asset","Rigging",["maya"],["Rough Draft", "Final"]))
	depts.append(Department("tex","asset","Textures",["mari","file"],["Rough Draft", "Final"]))
	depts.append(Department("material","asset","Materials",["hou"],["Rough Draft", "Final"]))
	depts.append(Department("groom","asset","Grooming",["maya","hou"],["Rough Draft", "Final"]))
	depts.append(Department("cloth","asset","Cloth",["maya","hou"],["Rough Draft", "Final"]))
	depts.append(Department("layout","shot","Layout",["maya","hou"],["Rough Draft", "Final"]))
	depts.append(Department("anim","shot","Animation",["maya"],["Rough Draft", "Final"]))
	depts.append(Department("fx","shot","VFXUserRoot",["hou"],["Rough Pass", "In Context", "Lit" ,"Final"]))
	depts.append(Department("sim","shot","Simulation",["maya","hou"],["Rough Draft", "Final"]))
	depts.append(Department("lighting","shot","Lighting",["maya","hou"],["Rough Draft", "Final"]))
	depts.append(Department("render","shot","Render",["file"],["Previs", "Final"]))
	depts.append(Department("comp","shot","Compositing",["nuke"],["Rough Draft", "Final"]))
	return depts

def CurrentProduction():
	return Production("Death and Delilah", getDepartments(), getPrograms(), [("asset","Asset"),("shot","Shot")])

def checkSyncConflictBody(path, user):
	"""
	Compares SyncFile with histories on the body & last modified on each file within
	each department and returns a list of conflicting files
	"""
	return ["path/to/file/model.mb","path/to/file/texture.tex"]
