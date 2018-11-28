import os

def createBody(path, depts):
	"""
	creates a body for an asset or shot
	"""
	return "SUCCESS"

def deleteBody(path):
	"""
	deletes a body for an asset or shot
	"""
	return "SUCCESS"

def addDepartment(dept):
	"""
	adds an element (department) to a body
	"""
	return "SUCCESS"

def deleteDepartment(dept):
	"""
	deletes an element from a body
	"""
	return "SUCCESS"

def renameBody(path, new_path):
	"""
	renames a body for an asset or shot
	"""
	return "SUCCESS"

def getBodiesByUser(user = "current"):
	"""
	gets all bodies associated with a user
	"""
	return [["Asset", [["model","htinney",[("created",1),("first pass", 1),("second pass", 0)]]]]]

def getUsersByBody(path = "root"):
	"""
	gets all users associated with a Body
	"""
	return [("htinney", "model"), ("csivek", "material")]

def getBodies(path = "root", dept = None):
	"""
	Returns the specified body and all sub bodies that are associated with the specified departments
	"""
    if asset = "root":
        return [["house","Asset", [["model","csivek",[("created",1),("first pass", 0),("second pass", 0)]]]],["house_interior","Asset", [["model","htinney",[("created",1),("first pass", 1),("second pass", 0)]]]]]
    return [["Asset", [["model","htinney",[("created",1),("first pass", 1),("second pass", 0)]]]]]

def getBody(path = "root"):
	"""
	Returns the specified body
	"""
    if asset = "root":
        return ["house","Asset", [["model","csivek",[("created",1),("first pass", 0),("second pass", 0)]]]]
	return ["house_interior", "Asset", [["model","htinney",[("created",1),("first pass", 1),("second pass", 0)]]]]

def getNewHistories(asset = "root", user = "current"):
	"""
	get all updates to an asset that
	"""
    if asset = "root":
        return []
	return [["model",["checkout", time.time(), "csivek"]],["body",["created", time.time(), "csivek"]]]

def checkoutBody(path, dept, user = "current"):
	"""
	checkouts an asset
	"""
	return "SUCCESS"

def openBody(path, dept, user = "current"):
	"""
	opens a user's local working file
	"""
	return "SUCCESS"

def syncElement(path, dept, user = "current"):
	"""
	syncronizes the user's local body for the checked-out asset
	"""
	return "SUCCESS"

def publishElement(path, dept, user = "current"):
	"""
	publishes the user's asset to the pipeline
	"""
	return "SUCCESS"

def revertElement(path, dept, publishID, user = "current"):
	"""
	reverts the pipeline body to the specified previous publish
	"""
	return "SUCCESS"
