
from .body import Body
from .element import Element
from .history import History
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
