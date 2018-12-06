
from .body import Body
from .element import Element
from .history import History
from .program import Program
import time

def getBodiesByUser(user = "current"):
	"""
	gets all bodies associated with a user
	"""
	bodies = []
	bodies.append(Body(getBodyTypes()[0],"house/interior/plant", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"office/interior/plant", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"house/exterior/fruit", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"chair", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"chairA", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"chairB", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"tables/broken_table", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"characters/grendy", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[0],"characters/delilah", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"house/interior/plants", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"office/interior/plants", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"house/exterior/fruits", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"chairs", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"chairAs", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"chairBs", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"tables/broken_tables", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"characters/grendys", ["model", "material"], user))
	bodies.append(Body(getBodyTypes()[1],"characters/delilahs", ["model", "material"], user))
	return bodies

def getBodyTypes():
	return [("ASSET","Asset"),("SHOT","Shot")]

def getBodies(path = "root", dept = None):
	"""
	Returns the specified body and all sub bodies that are associated with the specified departments
	"""
	body1 = Body(getBodyTypes()[0],"house/interior/plant", ["model", "material"], "csivek")
	body2 = Body(getBodyTypes()[1],"house/interior", ["model"], "htinney")
	if path == "root":
		return [body1,body2]
	return [body1]

def getBody(path = "root"):
	"""
	Returns the specified body
	"""
	body1 = Body(getBodyTypes()[0], path, ["model", "material"], user)
	body2 = Body(getBodyTypes()[0], "house/interior", ["model"], "htinney")
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
