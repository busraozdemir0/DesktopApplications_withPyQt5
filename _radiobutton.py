import sys
from PyQt5 import QtWidgets
from _radiobuttonForm import Ui_MainWindow

# pyuic5 _radiobuttonForm.ui -o _radiobuttonForm.py

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True) # çalıştırdığımızda varsayılan olarak Türkiye seçili olur
        self.ui.radioLise.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzer.toggled.connect(self.onClickedUlke)
        self.ui.radioYunanistan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)

        self.ui.radioilkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)


    def onClickedUlke(self):
        rb=self.sender()
        if rb.isChecked():
            print("Seçilen ülke: "+rb.text())

    def onClickedEgitim(self):
        rb=self.sender()
        if rb.isChecked():
            print("Seçilen eğitim: "+rb.text())

    def getSelectedUlke(self):
        items=self.ui.groupUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText("Seçilen ülke: "+rb.text())
    
    def getSelectedEgitim(self):
        items=self.ui.groupEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText("Seçilen eğitim: "+rb.text())

app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())