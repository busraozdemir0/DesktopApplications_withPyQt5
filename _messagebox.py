import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _messageboxForm import Ui_MainWindow

# pyuic5 _messageboxForm.ui -o _messageboxForm.py

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.ShowDialog)

    def ShowDialog(self):
        # 1. yöntem (kısa hali)
        result=QMessageBox.question(self,"Close Application","Are You Sure?",QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,QMessageBox.Cancel)
        if result==QMessageBox.Ok:
            print("Yes clicked")
            QtWidgets.qApp.quit()
        else:
            print("No clicked")

        # 2. yöntem (uzun hali)
        # msg=QMessageBox()

        # msg.setWindowTitle("Close Application")
        # msg.setText("Are you sure?")
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore) # altına butonlar eklemiş olduk
        # msg.setDefaultButton(QMessageBox.Ok) # butonlardan Ok olanı varsayılan seçili gelsin
        # msg.setDetailedText("details...")
        # msg.buttonClicked.connect(self.popup_button)
       
        # x=msg.exec_()
        # print(x)

    # def popup_button(self, i): # hangi butona tıklanırsa o butonun text bilgisini gösterir
    #     print(i.text())

    #     if i.text()=="OK":
    #         print("OKEY...")
    #         QtWidgets.qApp.quit() # Ok'a basıldığında form kapanır(uygulamayı sonlandırır)
    #     elif i.text()=="Cancel":
    #         print("Cancel...")
    #     else:
    #         print("Ignore...")


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())

app()