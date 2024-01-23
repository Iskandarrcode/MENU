from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from register import Register
from login import Login
import sys


class Asosiy(QMainWindow):
    def  __init__(self):
        QMainWindow.__init__(self)
        oyna = QWidget()
        self.resize(1920, 1080)
        self.setWindowTitle("Facebook")
        self.setStyleSheet("background-color: rgb(8, 102, 255)")


        mainver = QVBoxLayout()
        labelver = QHBoxLayout()
        lbl = QLabel()
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setText("Facebook")
        lbl.setStyleSheet("color: white")
        lbl.setFont(QFont("Montserrat", 50))



        mainver.addStretch()
        labelver.addWidget(lbl)
        mainver.addLayout(labelver)

        btnhor = QHBoxLayout()
        btnhor.setAlignment(Qt.AlignCenter)

        btnlog = QPushButton("      Login      ")
        btnlog.setStyleSheet("""background-color: #D4DEE5;
                             border-radius: 10px;
                             border: 2px;""")
        btnlog.setFont(QFont("Montserrat", 25))


        btnreg = QPushButton("    Register    ")
        btnreg.setStyleSheet("""background-color: #D4DEE5;
                             border-radius: 10px;
                             border: 2px;""")
        btnreg.setFont(QFont("Montserrat", 25))

        metalbl = QLabel("Meta © 2024")
        metalbl.setAlignment(Qt.AlignCenter)
        metalbl.setStyleSheet("""color: white;""")
        metalbl.setFont(QFont("Montserrat", 15))

        metahor = QHBoxLayout()
        metahor.addWidget(metalbl)

        btnhor.addStretch()
        btnhor.addStretch()

        btnhor.addWidget(btnlog)
        btnhor.addStretch()
        btnhor.addWidget(btnreg)
        btnhor.addStretch()
        btnhor.addStretch()

        mainver.addLayout(btnhor)
        mainver.addStretch()

        mainver.addLayout(metahor)
        oyna.setLayout(mainver)
        self.setCentralWidget(oyna)

        btnreg.clicked.connect(lambda: self.register())
        btnlog.clicked.connect(lambda: self.login())



    def login(self):
        self.login = Login()
        self.close()
        self.login.show()


    def register(self):
        self.register = Register()
        self.close()
        self.register.show()






app = QApplication([])
dastur = Asosiy()
dastur.show()
sys.exit(app.exec_())