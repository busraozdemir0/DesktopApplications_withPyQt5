import sys    # Komut satırından çalıştıracağımız için
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window(): # Bu fonksiyon bizim için bir pencere oluşturacak. Bu pencereye butonlar textbox'lar vs koyabiliriz.
    app=QApplication(sys.argv)
    win=QMainWindow()

    win.setWindowTitle("First Application") # pencere başlığı
    win.setGeometry(200,200,500,500) # pencere boyutlandırmak için
    win.setWindowIcon(QIcon("apple_icon.png")) # Başlığın yanındaki logoyu apple logosu yaptık
    win.setToolTip("my tooltip") # mouse ile pencere üzerine geldiğimizde my tooltip yazar

    win.show()
    sys.exit(app.exec_()) # çarpı ikonuna tıkladığımızda uygulamamız duracaktır.

window()