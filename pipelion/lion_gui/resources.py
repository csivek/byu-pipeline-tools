import sys
import os

class PipelionResources():
    @staticmethod
    def pipelionDirectory():
        try:
            pipelionLoc = os.environ["BYU_TOOLS_DIR"] + "/pipelion"
            return pipelionLoc
        except:
            return ""

    def appName(self):
        return "Pipelion"

    def showTitle(self):
        return "Death and Delilah"

    def logo(self):
        return  PipelionResources.pipelionDirectory() + "/images/PipelionLogoRevised.png"

    def logoSize(self):
        return 85

    def bodyTypes(self):
        return ["asset", "shot"]

    def BodyTypeNiceName(self, bodyType):
        if bodyType == "asset":
            return "Assets"
        return "Shots"

    #TODO: Futureproof this so that it takes in the asset types
    def departments(self, type=""):
        if type=="asset":
            return self.assetDepartments()
        elif type=="shot":
            return self.shotDepartments()

    def DepartmentNiceName(self, department):
        if department=="model":
            return "Modeling"
        elif department=="rig":
            return "Rigging"
        elif department=="materials":
            return "Materials"
        elif department=="groom":
            return "Grooming"
        elif department=="cloth":
            return "Cloth"
        elif department=="layout":
            return "Layout"
        elif department=="anim":
            return "Animation"
        elif department=="fx":
            return "VFX"
        elif department=="sim":
            return "Simulation"
        elif department=="lighting":
            return "Lighting"
        elif department=="comp":
            return "Composition"

    def assetDepartments(self):
        return ["model", "rig", "materials", "groom", "cloth"]

    def shotDepartments(self):
        return ["layout", "anim", "fx", "sim", "lighting", "comp"]

    def isAdmin(self):
        return True

class Strings():
    dashboard = "Dashboard"
    settings = "Settings"
    admin_tools = "Admin Tools"
    shortcuts = "Shortcuts"
    checkedoutitems = "Checked Out Items"
    open = "Open"
    sync = "Sync"
    nochanges = "No Changes"
    delete = "Delete"
    rename = "Rename"
    change_dot_dot_dot = "Change..."
    items = "Items"
    broken_data = "Broken Data"

class Styles():
    openButton = '''
        background-color: yellow
    '''
    syncButton = '''
        background-color: green
    '''
    deleteButton = '''
        background-color: red;
        color: white
    '''
    renameButton = '''
        background-color: purple;
        color: white
    '''
    changeButton = '''
        background-color: orange
    '''
