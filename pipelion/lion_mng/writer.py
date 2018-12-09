import os
import sys
from .production import Directories
from .logger import Logger
from body import Body
from .reader import *
from .files import *



def cloneDataToUser(body, user):
	userBody = Body(UserRoot(user), body.type, body.path)
	userBody.initializeDepartments(body.getDepartments())
	copy_directory(body.getMyLocation(), userBody.getMyLocation())
	userBody.writeSelfToFile()


def renameBody(old_body, new_path):
	renamedBody = Body(old_body.root, old_body.type, new_path)
	renamedBody.initializeDepartments(old_body.getDepartments())
	copy_directory(old_body.getMyLocation(), renamedBody.getMyLocation())
	renamedBody.writeSelfToFile()
	old_body.selfDestruct()
	return "SUCCESS"

def addDepartment(dept):
	"""
	adds an element (department) to a body
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def deleteDepartment(dept):
	"""
	deletes an element from a body
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def insertStep(dept, step, index):
	"""
	adds an element (department) to a body
	get current Production
	find Department in Production
	call Department.deleteStep()
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def renameStep(dept, oldStep, newStep):
	"""
	adds an element (department) to a body
	deleteStep()
	addStep()
	BUT PRESEVE THE STEP INFO BY ASSET
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def deleteStep(dept, step):
	"""
	deletes an step from a body
	get current Production
	find Department in Production
	call Department.deleteStep()
	Kendra
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
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def syncElement(path, dept, isMerge=False):
	"""
	if isMerge is false, Copy the production version of the file and replace the local one
	else Copy the production into a new file and flag the local Body for conflicts
	"""
	Logger.logUpdate()
	return "SUCCESS"

def publishElement(path, dept, user = "current"):
	"""
	publishes the user's asset to the pipeline
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def revertElement(path, dept, publishID, user = "current"):
	"""
	reverts the pipeline body to the specified previous publish
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"
