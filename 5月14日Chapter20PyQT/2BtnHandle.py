# -*- coding: cp936 -*-
import sys
from PyQt4 import QtCore, QtGui,uic #���������PyQt��

form_class = uic.loadUiType("MyFirstGui.ui")[0]  #���ص���һ���б�
print uic.loadUiType("MyFirstGui.ui")
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        x = self.pushButton.x()
        y = self.pushButton.y()
        x += 50
        y += 50
        self.pushButton.move(x,y)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()

app = QtGui.QApplication(sys.argv)  #�����¼�ѭ����PyQt����
myWindow = MyWindowClass() #����һ���������ʵ��
myWindow.show()
app.exec_()
