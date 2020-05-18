from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblPfad = QtWidgets.QLabel(self.centralwidget)
        self.lblPfad.setGeometry(QtCore.QRect(40, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblPfad.setFont(font)
        self.lblPfad.setObjectName("lblPfad")
        self.lblText = QtWidgets.QLabel(self.centralwidget)
        self.lblText.setGeometry(QtCore.QRect(70, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblText.setFont(font)
        self.lblText.setObjectName("lblText")
        self.txtPfad = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPfad.setGeometry(QtCore.QRect(260, 40, 371, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtPfad.setFont(font)
        self.txtPfad.setObjectName("txtPfad")
        self.txtText = QtWidgets.QLineEdit(self.centralwidget)
        self.txtText.setGeometry(QtCore.QRect(260, 90, 371, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtText.setFont(font)
        self.txtText.setObjectName("txtText")
        self.btbEinfuegen = QtWidgets.QPushButton(self.centralwidget)
        self.btbEinfuegen.setGeometry(QtCore.QRect(130, 200, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btbEinfuegen.setFont(font)
        self.btbEinfuegen.setObjectName("btbEinfuegen")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 300, 731, 201))
        self.textEdit.setObjectName("textEdit")
        self.btbAusgabe = QtWidgets.QPushButton(self.centralwidget)
        self.btbAusgabe.setGeometry(QtCore.QRect(440, 200, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btbAusgabe.setFont(font)
        self.btbAusgabe.setObjectName("btbAusgabe")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblPfad.setText(_translate("MainWindow", "Pfad des Bildes: "))
        self.lblText.setText(_translate("MainWindow", "GeheimText: "))
        self.btbEinfuegen.setText(_translate("MainWindow", "Einfügen"))
        self.btbAusgabe.setText(_translate("MainWindow", "Ausgabe"))
        self.btbEinfuegen.clicked.connect(self.einfuegen)
        self.btbAusgabe.clicked.connect(self.ausgabe)

    def einfuegen(self):

            pfad=self.txtPfad.text()
            text=self.txtText.text()

            f=open(pfad, encoding="ISO-8859-1")

            try:
                f=open(pfad, encoding="ISO-8859-1", mode="a+")
                f.write(" "+text)
                f=open(pfad, encoding="ISO-8859-1")

            finally:
                pass

    def ausgabe(self):
        pfad=self.txtPfad.text()
        f=open(pfad, encoding="ISO-8859-1")

        try:
            byte=f.read(1)
            str=""

            while byte!="":
                str=str+byte
                byte=f.read(1)

            self.textEdit.setText(str)



        finally :
            pass






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
