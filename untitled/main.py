# -*- coding: utf-8 -*-
import sys
from pyqtwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer
from pyfirmata import Arduino, util
import time
import serial

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.progressBar.setValue(58)
        self.radioButton.toggled.connect(self.radioButtonState)
        self.a_qtimer = QTimer()
        self.a_qtimer.timeout.connect(self.tick)
        self.a_qtimer.start(10)
        self.lineEdit.textChanged.connect(self.changeSerialPort)
        self.old_com="COM"
        

        """
        self.pushButton.clicked.connect(self.buttonClicked2)
    def buttonClicked2(self):
        print("buton pressed")
        """
        
    def radioButtonState(self):
        if self.radioButton.isChecked():
            print("Checked")
        else:  
            print("Unchecked")
            self.progressBar_1.setValue(0)
            self.progressBar_2.setValue(0)
            self.progressBar_3.setValue(0)
            self.progressBar_4.setValue(0)
            self.progressBar_5.setValue(0)
            self.progressBar_6.setValue(0)
            self.progressBar_7.setValue(0)

    def tick(self):
        warning_msg = QMessageBox()
        const1=180
        const2=0
        if self.radioButton.isChecked():
            try:
                data=self.msge7_data.readline().split()
                if (len(data)==7):
                    values=[int(j) for j in data]
                    self.progressBar_1.setValue(const1*values[0]/sum(values)+const2)
                    self.progressBar_2.setValue(const1*values[1]/sum(values)+const2)
                    self.progressBar_3.setValue(const1*values[2]/sum(values)+const2)
                    self.progressBar_4.setValue(const1*values[3]/sum(values)+const2)
                    self.progressBar_5.setValue(const1*values[4]/sum(values)+const2)
                    self.progressBar_6.setValue(const1*values[5]/sum(values)+const2)
                    self.progressBar_7.setValue(const1*values[6]/sum(values)+const2)
            except:
                self.radioButton.setChecked(False)
                warning_msg.warning(self, 'Message', "Input a Number", QMessageBox.Ok )

    def changeSerialPort(self):
        warning_msg = QMessageBox()
        com="COM"
        com=com+self.lineEdit.text()

        print(com)
        if (self.old_com!=com):
            if self.radioButton.isChecked():
                self.radioButton.setChecked(False)
            
            try:
                if len(com) >3 :
                    try:
                        self.msge7_data=serial.Serial(com,9600)
                        self.old_com=com
                            
                    except:
                        warning_msg.warning(self, 'Message', "Can't open"+com, QMessageBox.Ok )
            except:
                warning_msg.warning(self, 'Message', "Input a Number", QMessageBox.Ok )
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())