# -*- coding: cp936 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
#reload(sys)
#sys.setdefaultencoding('utf-8') ���ַ����벻ͬ��ʹ��

form_class = uic.loadUiType("tempconv.ui")[0]  #���ܴ򲻿���ԭ����������ʹ�õ��ַ�������python��ͬ��Ҫ����sys�ı���
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btn_CtoF_clicked) #�������¼���������������
        self.btnFtoC.clicked.connect(self.btn_FtoC_clicked)

    def btn_CtoF_clicked(self):
        cel = float(self.editCel.text())
        fahr = cel*9/5.0 + 32
        self.spinFahr.setValue(int(fahr+0.5))

    def btn_FtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32)*5/9.0
        cel_text = '%.2f'%cel
        self.editCel.setText(cel_text)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()

