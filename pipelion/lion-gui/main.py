import sys
import os
try:
    from PySide import QtGui as QtWidgets
    from PySide import QtGui as QtGui
    from PySide import QtCore
    from PySide.QtCore import Slot
except ImportError:
    from PySide2 import QtWidgets, QtGui, QtCore
    from PySide2.QtCore import Slot

# Adapted from https://stackoverflow.com/questions/50578661/how-to-implement-vertical-tabs-in-qt
class TabBar(QtWidgets.QTabBar):
    def __init__(self):
        super(TabBar, self).__init__()

    def tabSizeHint(self, index):
        size = super(TabBar, self).tabSizeHint(index)
        size.transpose()
        return size

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(0, self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            size = opt.rect.size()
            size.transpose()
            r = QtCore.QRect(QtCore.QPoint(), size)
            h = opt.rect.height()
            r.moveCenter(opt.rect.center() + QtCore.QPoint(0,(h / 2)))
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
            painter.restore()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.setTabBar(TabBar())
        self.setTabPosition(QtWidgets.QTabWidget.West)


app = QtWidgets.QApplication(sys.argv)
w = TabWidget()
w = QtWidgets.QTabWidget()
tabBar = TabBar()
w.setTabBar(tabBar)
w.setStyleSheet("Text-align:left");
w.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)

w.addTab(QtWidgets.QWidget(), "Dashboard")
w.addTab(QtWidgets.QWidget(), "Dashboard")
w.addTab(QtWidgets.QWidget(), "Settings")
w.addTab(QtWidgets.QWidget(), "Admin Tools")

w.show()

app.exec_()
