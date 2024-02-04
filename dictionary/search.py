from PyQt5.QtWidgets import QWidget, QRadioButton, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout

class searchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_rbtn_lay = QHBoxLayout()
        self.h_edit_lay = QHBoxLayout()

        self.en_rbtn = QRadioButton("EN-UZ")
        self.uzb_rbtn = QRadioButton("UZ-EN")

        self.h_rbtn_lay.addWidget(self.en_rbtn)
        self.h_rbtn_lay.addWidget(self.uzb_rbtn)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Search...")
        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.OK)

        self.h_edit_lay.addWidget(self.edit)
        self.h_edit_lay.addWidget(self.ok_btn)

        self.lbl = QLabel()

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.MENU)

        self.v_main_lay.addLayout(self.h_rbtn_lay)
        self.v_main_lay.addLayout(self.h_edit_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)

    def MENU(self):
        self.hide()

    def EN(self):
        file = open("baza.txt", "r")
        tekshir = False
        for i in file.read().split("\n"):
            i = i.split("-")
            if i[0] == self.edit.text():
                self.lbl.setText(i[1])
                tekshir = True
                break
        if tekshir == False:
            self.lbl.setText("Bu so'z lug'atingizda mavjud emas!")
        
        file.close()

    def UZ(self):
        file = open("baza.txt", "r")
        tekshir = False
        for i in file.read().split("\n"):
            i = i.split("-")
            if i[1] == self.edit.text():
                self.lbl.setText(i[0])
                tekshir = True
                break
        if tekshir == False:
            self.lbl.setText("Bu so'z lug'atingizda mavjud emas!")

        file.close()

    def OK(self):
        if self.en_rbtn.isChecked():
            self.EN()
        elif self.uzb_rbtn.isChecked():
            self.UZ()
        