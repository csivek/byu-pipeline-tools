from tables import *
import pipelion.lion_file_mng_dummy.production_reader as pr
from resources import *
from dialogs import *

class ViewModel():
    def __init__(self, parentWidget):
        self.userBodies = pr.getBodiesByUser()
        self.allBodies = pr.getBodies()
        self.parentWidget = parentWidget

    def loop(self):
        while True:
            #Ping the production manager
            print("This is supposed to ping the production manager")

    def checkedOutTable(self):
        tableData = {}
        for body in self.userBodies:
            controller = CheckoutEntryController(self.parentWidget, body)
            row = []
            row.append(self.labelEntry(body._path))
            row.append(self.buttonEntry(Strings().open, Styles().openButton, controller.showOpenBodyDialog))
            newHistories = pr.getNewHistories(body._path)
            if len(newHistories) > 0:
                row.append(self.buttonEntry(Strings().sync, Styles().syncButton, controller.showSyncBodyDialog))
            else:
                row.append(self.labelEntry(Strings().nochanges))
            row.append(self.buttonEntry(Strings().delete, Styles().deleteButton, controller.showDeleteBodyDialog))
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
