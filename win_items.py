import sys    # Komut satırından çalıştıracağımız için
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setWindowTitle("First Application") # pencere başlığı
        self.setGeometry(200,200,500,500) # pencere boyutlandırmak için
        self.setWindowIcon(QIcon("apple_icon.png")) # Başlığın yanındaki logoyu apple logosu yaptık
        self.setToolTip("my tooltip") # mouse ile pencere üzerine geldiğimizde my tooltip yazar
        self.initUI()

    def initUI(self):
        self.lbl_name=QtWidgets.QLabel(self) # label window'un bir elemanı olsun
        self.lbl_name.setText("Adınız: ") # pencere üzerine Adınız yazan text eklenecek
        self.lbl_name.move(50,30) # text'i konumlandırmak için

        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50,70)

        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(120,140)

        self.txt_name=QtWidgets.QLineEdit(self) # textbox eklemek için
        self.txt_name.move(120,30)
        self.txt_name.resize(200,32) # genişliğini ayarladık

        self.txt_surname=QtWidgets.QLineEdit(self)
        self.txt_surname.move(120,70)
        self.txt_surname.resize(200,32)

        self.btn_save=QtWidgets.QPushButton(self) # buton oluşturmak için
        self.btn_save.setText("Kaydet")
        self.btn_save.move(120,110)
        self.btn_save.clicked.connect(self.clicked) # butona tıklandığında clicked adlı metot çağrılacak ve metot içerisindeki ifade console'a yazılacak
    
    def clicked(self):
        self.lbl_result.setText("Ad: "+self.txt_name.text() +" Soyad: "+self.txt_surname.text())



def window(): # Bu fonksiyon bizim için bir pencere oluşturacak. Bu pencereye butonlar textbox'lar vs koyabiliriz.
    app=QApplication(sys.argv)
    win=MyWindow() # MyWindow adlı class sayesinde penceremiz oluşacak ve içerisine ilgili elemanlar eklenecek

    win.show()
    sys.exit(app.exec_()) # çarpı ikonuna tıkladığımızda uygulamamız duracaktır.

window()