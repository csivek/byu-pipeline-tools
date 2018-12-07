import os
import sys
import fcntl
import datetime
import traceback
import inspect
from .production import Directories
try:
    from PySide.QtCore import QThread, Slot, Signal
except ImportError:
    from PySide2.QtCore import QThread, Slot, Signal

# https://stackoverflow.com/questions/2823112/communication-between-threads-in-pyside
class Logger(QThread):
    productionUpdate = Signal(str)

    # https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
    def __init__(self, stopEvent):
        super(Logger, self).__init__()
        self.lastUpdatedLocal = datetime.datetime.now()
        self.stopped = stopEvent

    def run(self):
        while not self.stopped.wait(1):
            update = self.newUpdates()
            if(len(update) > 0):
                print("logger found a change:" + self.newUpdates())
                self.productionUpdate.emit(update)

    # https://stackoverflow.com/questions/3346430/what-is-the-most-efficient-way-to-get-first-and-last-line-of-a-text-file
    def newUpdates(self):
        time = datetime.datetime.now()
        lastUpdate = Logger.getLastLine()
        try:
            self.lastUpdatedProduction = datetime.datetime.strptime(lastUpdate.split()[0], "%Y-%m-%d%H:%M:%S.%f")
        except:
            return ""
        if self.lastUpdatedProduction > self.lastUpdatedLocal:
            self.lastUpdatedLocal = self.lastUpdatedProduction
            return lastUpdate
        else:
            return ""

    @staticmethod
    def logpath():
        return os.path.join(Directories.logDir(),"logs.txt")

    @staticmethod
    def _getFunctionName():
    	return traceback.extract_stack(None,3)[0][2]

    @staticmethod
    def _getFunctionParametersAndValues():
    	frame = inspect.currentframe().f_back.f_back
    	args,_,_,values = inspect.getargvalues(frame)
    	return ([(i,values[i]) for i in args])

    @staticmethod
    def logUpdate():
    	message = os.environ["USER"] + " " + Logger._getFunctionName() + " " + str(Logger._getFunctionParametersAndValues())
    	with open(Logger.logpath(), "a+") as f:
            #Cory TODO: Surround this in a try catch so that in case writing fails, the file isn't locked
    		fcntl.flock(f, fcntl.LOCK_EX)
    		f.write(str(datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S.%f")) + " " + message + "\n")
    		fcntl.flock(f, fcntl.LOCK_UN)
            #Cory TODO: truncate this list when there are too many lines
    		f.close()

    @staticmethod
    def getLastLine():
        with open(Logger.logpath(), "rb") as f:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b"\n":
                f.seek(-2, os.SEEK_CUR)
            last = f.readline()
            f.close()
            return last
