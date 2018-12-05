import sys
import os

class PipelionResources():
    def logo(self):
        return "../images/PipelionLogoRevised.png"

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
