# -*- coding: cp936 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
#reload(sys)
#sys.setdefaultencoding('utf-8') 若字符编码不同可使用


#######################
###QT中设置热键在title/text值前面添加&    &File F作为热键 E&xit X作为热键
form_class = uic.loadUiType("tempconvMenu.ui")[0]  #可能打不开，原因是里面我使用的字符编码与python不同，要设置sys的编码
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btn_CtoF_clicked)
        self.btnFtoC.clicked.connect(self.btn_FtoC_clicked)
        self.actionC_to_F.triggered.connect(self.btn_CtoF_clicked)#连接菜单项和事件处理函数
        self.actionF_to_C.triggered.connect(self.btn_FtoC_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)

    def btn_CtoF_clicked(self):
        cel = float(self.editCel.text())
        fahr = cel*9/5.0 + 32
        self.spinFahr.setValue(int(fahr+0.5))

    def btn_FtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32)*5/9.0
        cel_text = '%.2f'%cel
        self.editCel.setText(cel_text)

    def menuExit_selected(self):
        self.close()
        
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
