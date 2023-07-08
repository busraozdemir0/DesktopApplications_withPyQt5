import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from _checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitap.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnHobiSec.clicked.connect(self.getAllHobiler)
        self.ui.btnDersSec.clicked.connect(self.getAllDersler)

    def getAllHobiler(self):
        result=" "
        items=self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items: # her bir elemana tek tek ulaşıyoruz
            if cb.isChecked(): # sadece seçili olanlar gelmesi için kontrol
                result+=cb.text()+"\n" # seçilenleri label'a alt alta yazdıracağız
        self.ui.lblHobiResult.setText(result)

    def getAllDersler(self):
        result=" "
        items=self.ui.groupDersler.findChildren(QtWidgets.QCheckBox)
        for cb in items: # her bir elemana tek tek ulaşıyoruz
            if cb.isChecked(): # sadece seçili olanlar gelmesi için kontrol
                result+=cb.text()+"\n" # seçilenleri label'a alt alta yazdıracağız
        self.ui.lblDersResult.setText(result)

    def show_state(self,value):
        cb=self.sender() # seçilenin referansı

        print(value)
        print(cb.text()) # seçilen cb'nin text'i
        print(cb.isChecked()) # checkbox'ın seçilip seçilmediği bilgisi


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()