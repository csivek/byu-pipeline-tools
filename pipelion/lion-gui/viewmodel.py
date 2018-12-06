from tables import *
import pipelion.lion_file_mng_dummy.production_reader as pr
from resources import *
from dialogs import *

class ViewModel():
    def __init__(self):
        self.userBodies = pr.getBodiesByUser()
        self.allBodies = pr.getBodies()

    def loop(self):
        while True:
            #Ping the production manager
            print("This is supposed to ping the production manager")

    def checkedOutTable(self):
        tableData = {}
        for body in self.userBodies:
            row = []
            row.append(self.labelEntry(body._path))
            row.append(self.buttonEntry(Strings().open, Styles().openButton, lambda: Dialogs().showOpenBodyDialog(body._path)))
            newHistories = pr.getNewHistories(body._path)
            if len(newHistories) > 0:
                row.append(self.buttonEntry(Strings().sync, Styles().syncButton, lambda: Dialogs().showSyncBodyDialog(body._path)))
            else:
                row.append(self.labelEntry(Strings().nochanges))
            row.append(self.buttonEntry(Strings().delete, Styles().deleteButton, lambda: Dialogs().showDeleteCheckedOutBodyDialog(body._path)))
            tableData[body._path] = row

        headers = []
        headers.append(Strings().items)
        headers.append(Strings().open)
        headers.append(Strings().sync)
        headers.append(Strings().delete)
        return tableData, headers

    def bodyOverviewTable(self):
        tableData = {}
        for body in self.allBodies:
            row = []
            row.append(self.labelEntry(body._path))
            departmentsLabel = ""
            for element in body._elements:
                departmentsLabel += element.dept + " "
            row.append(self.buttonEntry(Strings().rename, Styles().renameButton, lambda: Dialogs().showRenameBodyDialog(body._path)))

    def departmentTable(self):
        tableData = {}

    def labelEntry(self, label):
        entry = {}
        entry["type"] = TableItemType().Label
        entry["label"] = label
        return entry

    def buttonEntry(self, label, style, action=None):
        entry = {}
        entry["type"] = TableItemType().Button
        entry["label"] = label
        entry["style"] = style
        if action is not None:
            entry["action"] = action
        return entry
