from PyQt5.QtWidgets import QWidget, QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

class listWIndow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_lbl_lay = QHBoxLayout()

        self.en_lbl = QLabel("English")
        self.uzb_lbl = QLabel("Uzbek")

        self.h_lbl_lay.addWidget(self.en_lbl)
        self.h_lbl_lay.addStretch()
        self.h_lbl_lay.addWidget(self.uzb_lbl)

        self.lwg = QListWidget()
        file = open("baza.txt", "r")
        file.seek(0)
        self.lst = sorted([i for i in file.read().split("\n")])
        self.lwg.addItems(self.lst)

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.MENU)

        self.v_main_lay.addLayout(self.h_lbl_lay)
        self.v_main_lay.addWidget(self.lwg)
        self.v_main_lay.addWidget(self.menu_btn)

        file.close()
        self.setLayout(self.v_main_lay)


    def MENU(self):
        self.hide()