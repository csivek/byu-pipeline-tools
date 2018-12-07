import os
import sys


class Production:
    def __init__(self, name, departments, programs, bodyTypes, logo=None):
        self.name = name
        self.departments = departments
        self.programs = programs
        self.bodyTypes = bodyTypes
        if logo:
            self.logo = logo
        else:
            self.logo = os.path.join(Directories.pipelionDir(),"icons","default-logo.png")

class Directories:
    @staticmethod
    def pipelionDir():
        try:
            return os.path.join(os.environ["BYU_TOOLS_DIR"],"pipelion")
        except:
            return ""

    @staticmethod
    def logDir():
        try:
            path = os.path.join(os.environ["BYU_PROJECT_DIR"],"production","logs")
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        except:
            return ""
