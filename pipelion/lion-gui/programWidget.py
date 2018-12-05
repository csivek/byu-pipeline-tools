#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys
import os
import random
from PySide2 import QtCore, QtWidgets, QtGui

class ProgramImageWidget(QtWidgets.QAbstractButton):
	def __init__(self, program, size, doubleClick=None, parent=None):
		super(ProgramImageWidget, self).__init__(parent)
        
		pipelionLoc = os.environ["BYU_TOOLS_DIR"] + "/pipelion"
		print(pipelionLoc + "/lion-gui/icons/hou.png")
		self.pixmap = QtGui.QPixmap(pipelionLoc + "/icons/hou.png")
		self.pixmap_hover = QtGui.QPixmap(pipelionLoc + "/icons/mari.png")
		self.pixmap_pressed = QtGui.QPixmap(pipelionLoc + "/icons/maya.png")

		self.pressed.connect(self.update)
		self.released.connect(self.update)

		self.size = size
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHeightForWidth(True)
		self.setSizePolicy(sizePolicy)
			
	def paintEvent(self, event):
		pix = self.pixmap_hover if self.underMouse() else self.pixmap
		if self.isDown():
			pix = self.pixmap_pressed

		painter = QtGui.QPainter(self)
		painter.drawPixmap(event.rect(), pix)

	def enterEvent(self, event):
		self.update()

	def leaveEvent(self, event):
		self.update()

	def sizeHint(self):
		return QtCore.QSize(self.size, self.size)

	def heightForWidth(self, width):
		return width

class ProgramWidget(QtWidgets.QWidget):
	def __init__(self, program, size, showLabel=False, doubleClick=None, parent=None):
		QtWidgets.QWidget.__init__(self)
		self.projectButton = ProgramImageWidget(program, size)
		self.text = QtWidgets.QLabel(program)
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.addWidget(self.projectButton)
		if (showLabel):
			self.layout.addWidget(self.text)
		self.setLayout(self.layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = ProgramWidget("My Program",200, showLabel=True)
    widget.show()

    sys.exit(app.exec_())
