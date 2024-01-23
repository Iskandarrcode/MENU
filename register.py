from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import re
import os
import uuid


class Register(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.__reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.resize(1920, 1080)
        self.setFont(QFont("Montserrat", 14))
        self.setWindowTitle("Register")
        oyna = QWidget(self)
        oyna.setGeometry(0, 0, 1920, 1080)
        oyna.setStyleSheet("""background-color: #4DB0F9""")
        

        self.name = QLabel("Name", self)
        self.name.setGeometry(835, 100, 300, 30)
        self.line_name = QLineEdit(self)
        self.line_name.setGeometry(835, 140, 300, 40)
        self.mes_name = QLabel(self)
        self.mes_name.setGeometry(1130, 140, 150, 40)
        self.mes_name.setStyleSheet("color: red; font-size: 20px;")

        self.surname = QLabel("Surname", self)
        self.surname.setGeometry(835, 190, 300, 30)
        self.line_surname = QLineEdit(self)
        self.line_surname.setGeometry(835, 230, 300, 40)
        self.mes_surname = QLabel(self)
        self.mes_surname.setGeometry(1130, 230, 150, 40)
        self.mes_surname.setStyleSheet("color: red; font-size: 20px;")

        self.email = QLabel("Email", self)
        self.email.setGeometry(835, 280, 300, 30)
        self.line_email = QLineEdit(self)
        self.line_email.setGeometry(835, 320, 300, 40)
        self.mes_email = QLabel(self)
        self.mes_email.setGeometry(1130, 320, 150, 40)
        self.mes_email.setStyleSheet("color: red; font-size: 20px;")

        self.password = QLabel("Password", self)
        self.password.setGeometry(835, 370, 300, 30)
        self.line_password = QLineEdit(self)
        self.line_password.setGeometry(835, 410, 300, 40)
        self.mes_password = QLabel(self)
        self.mes_password.setGeometry(1130, 410, 150, 40)
        self.mes_password.setStyleSheet("color: red; font-size: 20px;")


        self.re_password = QLabel("Repeat password", self)
        self.re_password.setGeometry(835, 460, 300, 30)
        self.line_re_password = QLineEdit(self)
        self.line_re_password.setGeometry(835, 500, 300, 40)
        self.mes_repass = QLabel(self)
        self.mes_repass.setGeometry(1130, 500, 150, 40)
        self.mes_repass.setStyleSheet("color: red; font-size: 20px;")

        self.btn = QPushButton("Register", self)
        self.btn.setGeometry(830, 570, 300, 50)
        self.btn.setStyleSheet("""background-color: #4DB0F9;
                                             border-radius: 22px;""")

        self.btn.clicked.connect(lambda: self.to_login())

    def to_login(self):
        self.lamp = True
        name = self.line_name.text().strip()
        surname = self.line_surname.text().strip()
        email = self.line_email.text().strip()
        password = self.line_password.text().strip()
        re_password = self.line_re_password.text().strip()

        if len(name) < 3:
            self.lamp = False
            self.mes_name.setText("invalid name")
        else:
            self.mes_name.setText("")

        if len(surname) < 3:
            self.lamp = False
            self.mes_surname.setText("invalid surname")
        else:
            self.mes_surname.setText("")

        if not (re.fullmatch(self.__reg, email)):
            self.lamp = False
            self.mes_email.setText("invalid email")
        else:
            self.mes_email.setText("")
        
        if not (password == re_password and len(password) > 4):
            self.lamp = False

            self.mes_repass.setText("invalid password")
        else:
            self.mes_repass.setText("")


        if self.lamp:
            self.write(name, surname, email, password)

    def write(self, name, surname, email, password):
        if  not os.path.exists("baza.txt"):
            file = open("baza.txt", "x")
            file.close()

        with open("baza.txt", "a") as f:
            f.write(f"{self.generate_id()}#{name}#{surname}#{email}#{password}\n")


    def generate_id(self):
        return uuid.uuid1()
        


        