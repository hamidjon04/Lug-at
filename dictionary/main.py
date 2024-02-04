from PyQt5.QtWidgets import QApplication
from mainwindow import MyWindow


app = QApplication([])
mainWindow = MyWindow()


mainWindow.show()
app.exec_()