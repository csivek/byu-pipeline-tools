import os
import sys
from .production import Directories
from .logger import Logger

def createBody(path, depts):
	"""
	creates a body for an asset or shot
	"""
	Logger.logUpdate()
	return "SUCCESS"

def deleteBody(path):
	"""
	deletes a body for an asset or shot
	"""
	Logger.logUpdate()
	return "SUCCESS"

def renameBody(path, new_path):
	"""
	renames a body for an asset or shot
	"""
	Logger.logUpdate()
	return "SUCCESS"

def addDepartment(dept):
	"""
	adds an element (department) to a body
	"""
	Logger.logUpdate()
	return "SUCCESS"

def deleteDepartment(dept):
	"""
	deletes an element from a body
	"""
	Logger.logUpdate()
	return "SUCCESS"

def insertStep(dept, step, index):
	"""
	adds an element (department) to a body
	get current Production
	find Department in Production
	call Department.deleteStep()
	"""
	Logger.logUpdate()
	return "SUCCESS"

def renameStep(dept, oldStep, newStep):
	"""
	adds an element (department) to a body
	deleteStep()
	addStep()
	BUT PRESEVE THE STEP INFO BY ASSET
	"""
	Logger.logUpdate()
	return "SUCCESS"

def deleteStep(dept, step):
	"""
	deletes an step from a body
	get current Production
	find Department in Production
	call Department.deleteStep()
	"""
	#Kendra TODO: Add Backend Calls to change steps in each element of bodies
	Logger.logUpdate()
	return "SUCCESS"

def moveStep(dept, step, index):
	"""
	deletes an element from a body
	get current Production
	find Department in Production
	call Department.moveStep()
	"""
	Logger.logUpdate()
	return "SUCCESS"

def checkoutBody(path, dept, user = "current"):
	"""
	checkouts an asset
	"""
	Logger.logUpdate()
	return "SUCCESS"

def openBody(path, dept, user = "current"):
	"""
	opens a user's local working file
	"""
	Logger.logUpdate()
	return "SUCCESS"

def syncElement(path, dept, user = "current"):
	"""
	syncronizes the user's local body for the checked-out asset
	"""
	Logger.logUpdate()
	return "SUCCESS"

def publishElement(path, dept, user = "current"):
	"""
	publishes the user's asset to the pipeline
	"""
	Logger.logUpdate()
	return "SUCCESS"

def revertElement(path, dept, publishID, user = "current"):
	"""
	reverts the pipeline body to the specified previous publish
	"""
	Logger.logUpdate()
	return "SUCCESS"
