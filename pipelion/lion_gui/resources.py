import sys
import os
import pipelion.lion_mng.reader as Reader

class PipelionResources():

    @staticmethod
    def appName():
        return "Pipelion"

    @staticmethod
    def showTitle():
        return Reader.CurrentProduction().name

    @staticmethod
    def logo():
        return Reader.CurrentProduction().logo

    @staticmethod
    def logoSize():
        return 85
        
    @staticmethod
    def bodyTypes():
        return Reader.CurrentProduction().bodyTypes

    @staticmethod
    def departments(type=("","")):
        if type == ("",""):
            return Reader.CurrentProduction().departments
        else:
            return [x for x in Reader.CurrentProduction().departments if x.type == type[0]]

    @staticmethod
    def isAdmin():
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
