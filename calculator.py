#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 23:57:30 2022

@author: ziyasarican
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        
        self.setWindowTitle("Calculator")
        self.setGeometry(150,150,450,300)
        self.initUI()
        
        
    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Number 1: ")
        self.lbl_num1.move(30,20)
        
        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Number 2: ")
        self.lbl_num2.move(30,60)
        
        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(100,20)
        
        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(100,60)
            
        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("Add")
        self.btn_add.move(30,120)
        self.btn_add.clicked.connect(self.calculate)
        
        self.btn_substract = QtWidgets.QPushButton(self)
        self.btn_substract.setText("Substract")
        self.btn_substract.move(130,120)
        self.btn_substract.clicked.connect(self.calculate)
        
        self.btn_divide = QtWidgets.QPushButton(self)
        self.btn_divide.setText("Divide")
        self.btn_divide.move(230,120)
        self.btn_divide.clicked.connect(self.calculate)
        
        self.btn_multiply = QtWidgets.QPushButton(self)
        self.btn_multiply.setText("Multiply")
        self.btn_multiply.move(330,120)
        self.btn_multiply.clicked.connect(self.calculate)
        
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.setStyleSheet("border: 1px solid black;")
        self.lbl_result.resize(200,30)
        self.lbl_result.move(30,160)
        
    def calculate(self):
        sender = self.sender().text()
        
      
        result = 0
        
        try:
            num1 = int(self.txt_num1.text())
            num2 = int(self.txt_num2.text())
        except:
            self.lbl_result.setText("Please enter only number!")
        
        if (sender == "Add"):
            result = num1 + num2
        elif(sender == "Substract"):
            result = num1 - num2
        elif(sender == "Divide"):
            result = num1 / num2
        elif(sender == "Multiply"):
            result = num1 * num2
        
        self.lbl_result.setText("Result: " + str(result))
        self.lbl_result.move(30,160)
    
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
    
app()
