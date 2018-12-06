
from .body import Body
from .element import Element
from .history import History
from .program import Program
import time

def getBodiesByUser(user = "current"):
	"""
	gets all bodies associated with a user
	"""
	body = Body("house/interior/plant", ["model", "material"], user)
	elem = body.getElement("model")
	elem.assignUser(user)
	elem.setStep("first pass", 1)
	elem.setStep("created", 1)
	elem.setStep("second pass", 0)
	return [body]

def getBodies(path = "root", dept = None):
	"""
	Returns the specified body and all sub bodies that are associated with the specified departments
	"""
	body1 = Body("house/interior/plant", ["model", "material"], "csivek")
	body2 = Body("house/interior", ["model"], "htinney")
	if path == "root":
		return [body1,body2]
	return [body1]

def getBody(path = "root"):
	"""
	Returns the specified body
	"""
	body1 = Body(path, ["model", "material"], user)
	body2 = Body("house/interior", ["model"], "htinney")
	if path == "root":
		return body2
	return body1

def getNewHistories(path = "root", user = "current"):
	"""
	get all updates to an asset that
	"""
	if path == "root":
		return []
	return [History("model","CHECKOUT", time.time(), "csivek", "csivek checked out asset " + path),History("body","PUBLISH", time.time(), "csivek", "csived created asset " + path)]

def getPrograms():
	programs = []
	programs.append(Program("usd", "USDView", ["usd"], "icons/usd.png", "/opt/hfs.current/bin/usdview"))
	programs.append(Program("maya", "Maya", ["ma","mb"], "icons/maya.png", "app-launch-scripts/project_maya.sh"))
	programs.append(Program("hou", "Houdini", ["hip","hipnc"], "icons/hou.png", "app-launch-scripts/project_houdini.sh"))
	programs.append(Program("mari", "Mari", ["mari"], "icons/mari.png", "app-launch-scripts/project_mari.sh"))
	programs.append(Program("nuke", "Nuke", ["nk"], "icons/nuke.png", "app-launch-scripts/project_nuke.sh"))
	programs.append(Program("file", "Extra Files", ["*"], "icons/file.png", "app-launch-scripts/project_file.sh"))
	return programs
