from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

class AddWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.v_edit_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.en_edit = QLineEdit()
        self.en_edit.setPlaceholderText("English...")
        self.uzb_edit = QLineEdit()
        self.uzb_edit.setPlaceholderText("Uzbek...")

        self.v_edit_lay.addWidget(self.en_edit)
        self.v_edit_lay.addWidget(self.uzb_edit)

        self.add_btn = QPushButton("ADD")
        self.add_btn.clicked.connect(self.ADD)

        self.h_btn_lay.addLayout(self.v_edit_lay)
        self.h_btn_lay.addWidget(self.add_btn)

        self.lbl = QLabel()

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.MENU)

        self.v_main_lay.addLayout(self.h_btn_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)

    def ADD(self):
        if self.en_edit.text() == "" or self.uzb_edit.text() == "":
            self.lbl.setText("Oynalar to'ldirilmagan")
            self.en_edit.setText("")
            self.uzb_edit.setText("")
            return
        file = open("baza.txt", "a+")
        tekshir = False
        file.seek(0)
        for i in file.read().split("\n"):
            if self.en_edit.text() + "-" + self.uzb_edit.text() == i:
                tekshir = True
        if tekshir:
            self.lbl.setText("Lug'atda mavjud!")
        else:
            self.lbl.setText("Muvaffaqiyatli qo'shildi✅")
            file.write("\n" + self.en_edit.text() + "-" + self.uzb_edit.text())
            self.en_edit.setText("")
            self.uzb_edit.setText("")


        file.close()

    def MENU(self):
        self.hide()
