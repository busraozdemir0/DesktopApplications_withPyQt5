import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette=self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100,100,500,500)

        # layout=QtWidgets.QVBoxLayout() # layout tipi= verticle layout(her bir kutu/widget alt alta sıralanacak)
        
        # --- üstte 3 altta 2 kutucuk layoutu yapma ---
        hlayout=QtWidgets.QHBoxLayout() # Horizontal layout= yan yana sıralanır
        hlayout.addWidget(Color("red"))
        hlayout.addWidget(Color("blue"))
        hlayout.addWidget(Color("green"))
        #hlayout.setContentsMargins(50,0,0,0) # soldan 50 piksellik boşluk bırakacak
        #hlayout.setContentsMargins(50,0,0,30) # soldan 50, alttan 30 piksek boşluk bırakacak
        hlayout.setSpacing(30) # her eleman arasında 30 piksel boşluk bırakacak
       
        hlayout2=QtWidgets.QHBoxLayout() 
        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("green"))
        hlayout2.setSpacing(30)

        vlayout=QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addLayout(hlayout2)


        # --- Grid layout ---
        # layout=QtWidgets.QGridLayout() 
        # layout.addWidget(Color("red"),0,0) # 0'a 0'ıncı eleman olacak
        # layout.addWidget(Color("blue"),1,0)
        # layout.addWidget(Color("green"),0,2)
        # layout.addWidget(Color("yellow"),3,2)

        widget=QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

app()