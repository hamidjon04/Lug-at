from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from add import AddWindow
from list import listWIndow
from search import searchWindow

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
    
        self.h_main_lay = QHBoxLayout()
        self.v_btn_lay = QVBoxLayout()

        self.add_btn = QPushButton("ADD")
        self.add_btn.clicked.connect(self.ADD)
        self.list_btn = QPushButton("LIST")
        self.list_btn.clicked.connect(self.LIST)
        self.search_btn = QPushButton("SEARCH")
        self.search_btn.clicked.connect(self.SEARCH)
        self.exit_btn = QPushButton("EXIT")
        self.exit_btn.clicked.connect(exit)

        self.v_btn_lay.addWidget(self.add_btn)
        self.v_btn_lay.addWidget(self.list_btn)
        self.v_btn_lay.addWidget(self.search_btn)
        self.v_btn_lay.addWidget(self.exit_btn)

        self.h_main_lay.addStretch()
        self.h_main_lay.addLayout(self.v_btn_lay)
        self.h_main_lay.addStretch()

        self.setLayout(self.h_main_lay)

    def ADD(self):
        self.addWindow = AddWindow()
        self.addWindow.show()
        

    def LIST(self):
        self.listWindow = listWIndow()
        self.listWindow.show()

    def SEARCH(self):
        self.searchWindow = searchWindow()
        self.searchWindow.show()







