from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import sys


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.__reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.resize(1920, 1080)
        self.setFont(QFont("Montserrat", 15))
        self.setWindowTitle("Register")
        self.oyna = QWidget(self)
        self.oyna.setGeometry(0, 0, 1920, 1080)
        self.oyna.setStyleSheet("""background-color: #4DB0F9""")

        self.email = QLabel("Email", self)
        self.email.setGeometry(835, 250, 300, 30)
        self.line_email = QLineEdit(self)
        self.line_email.setGeometry(835, 290, 350, 40)
        self.mes_email = QLabel(self)
        self.mes_email.setGeometry(1130, 140, 150, 40)
        self.mes_email.setStyleSheet("color: red; font-size: 20px;")
        
        self.password = QLabel("Password", self)
        self.password.setGeometry(835, 370, 300, 30)
        self.line_password = QLineEdit(self)
        self.line_password.setGeometry(835, 410, 350, 40)
        self.mes_password = QLabel(self)
        self.mes_password.setGeometry(1130, 410, 150, 40)
        self.mes_password.setStyleSheet("color: red; font-size: 20px;")
        
        self.btn = QPushButton("Sabmit", self, clicked = lambda : self.to_loginn())
        self.btn.setGeometry(830, 530, 300, 50)
        self.btn.setStyleSheet("""background-color: #4DB0F9;
                                             border-radius: 22px;""")
        
        
    def to_loginn(self):
        
        self.lamp = True
        email = self.line_email.text().strip()
        password = self.line_password.text().strip()

        
        if not (re.fullmatch(self.__reg, email)):
            self.lamp = False
            self.mes_email.setText("invalid email")
        else:
            self.mes_email.setText("")
        
        if not (len(password) > 4):
            self.lamp = False
            self.mes_password.setText("invalid password")
        else:
            self.mes_password.setText("")


        if self.lamp:
            self.writee(email, password)

    def writee(self, email, password):
        file = open("baza.txt", "r")
        res = file.readlines()
        for i in res:
            i = i.split("#")
            psw = i[4][:-1]  
            if i[3] == email and psw == password:
                self.mes = QMessageBox(self.oyna)
                self.mes.resize(1920, 1080)
                self.mes.setWindowTitle("Hello ")
                self.mes.setText("Hello")
                self.mes.exec_()
                # self.btnn = QPushButton("Kirish", self.oyna)
                # self.btnn.setGeometry(0, 0, 1920, 1080)
                # self.btnn.setStyleSheet("""background-color: white;""") 
            
        file.close()
        