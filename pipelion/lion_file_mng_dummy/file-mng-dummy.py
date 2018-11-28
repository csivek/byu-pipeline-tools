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

def renameBody(path, new_path):
	"""
	renames a body for an asset or shot
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
