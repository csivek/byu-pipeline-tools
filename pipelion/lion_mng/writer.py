import os
import sys
from .production import Directories
from .logger import Logger
from body import Body
from .reader import *
from .files import *

def createBody(path, depts, type):
	"""
	creates a body for an asset or shot, and all of its corresponding metadata and directories
	"""
	body = Body(type, path, depts)
	body.writeSelfToFile()
	Logger.logUpdate()
	return body

#deletes the cloned body from a user's private folder (/groups/dand/users/....)
def deleteBodyClone(path, user):

	return "SUCCESS"

def renameBody(path, new_path):
	"""
	renames a body for an asset or shot
	Kendra
	"""
	Logger.logUpdate()
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

def openBody(path, dept, user = "current"):
	"""
	opens a user's local working file
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def cloneBody(path, dept, user = "current"):
	"""
	checkouts an asset, creates a SyncFile (a config file that gives the timestamp
	of when each department was cloned)
	Kendra
	"""
	Logger.logUpdate()
	return "SUCCESS"

def syncBody(path, depts, user = "current"):
	"""
	syncronizes the user's local body for the checked-out asset
	Replaces all departments of a body in a user's working directory that are
	passed in through "depts".
	Call syncElement on all non-conflicting Elements of a cloned local Body

	Creates a SyncFile (a config file that gives the timestamp of when the element was last synced)
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
