# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui,uic #导入所需的PyQt库

form_class = uic.loadUiType("tempconv.ui")[0]  #返回的是一个列表
print uic.loadUiType("MyFirstGui.ui")
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)  #返回事件循环的PyQt对象
myWindow = MyWindowClass() #创建一个窗口类的实例
myWindow.show()
app.exec_()
