#!/usr/bin/envpython3
# -*-coding: utf-8 -*-
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import cmath

class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()
    def interfejs(self):
        self.resize(3300, 3100)
        self.setWindowTitle("Super Kalkulator")
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)
        uklad = QGridLayout()
        uklad.addWidget(etykieta1, 0, 0)
        uklad.addWidget(etykieta2, 0, 1)
        uklad.addWidget(etykieta3, 0, 2)
        self.setLayout(uklad)
        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()
        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')
        uklad.addWidget(self.liczba1Edt, 1, 0)
        uklad.addWidget(self.liczba2Edt, 1, 1)
        uklad.addWidget(self.wynikEdt, 1, 2)
        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        dzielBtn = QPushButton("&Mnóż", self)
        mnozBtn = QPushButton("&Dziel", self)
        koniecBtn = QPushButton("&Koniec", self)
        potegaBtn = QPushButton("&Potega", self)
        pierwiastekBtn = QPushButton("&Pierwiastek", self)
        procentBtn = QPushButton("&Procent", self)
        odwrotnoscBtn = QPushButton("&Odwrotność",self)
        koniecBtn.resize(koniecBtn.sizeHint())
        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)
        ukladH.addWidget(pierwiastekBtn)
        ukladH.addWidget(potegaBtn)
        ukladH.addWidget(procentBtn)
        ukladH.addWidget(odwrotnoscBtn)
        uklad.addLayout(ukladH, 2, 0, 1, 3)
        uklad.addWidget(koniecBtn, 3, 0, 1, 3)

        koniecBtn.clicked.connect(self.koniec)
        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)
        pierwiastekBtn.clicked.connect(self.dzialanie)
        potegaBtn.clicked.connect(self.dzialanie)
        procentBtn.clicked.connect(self.dzialanie)
        odwrotnoscBtn.clicked.connect(self.dzialanie)

        self.show()


    def koniec(self):
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        odp = QMessageBox.question(self, 'Komunikat', "Czy na pewno koniec?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def dzialanie(self):
        nadawca = self.sender()
        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""
            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2            
            elif nadawca.text() == "&Odejmij":
                wynik = liczba1 - liczba2                    
            elif nadawca.text() == "&Mnóż":
                wynik = liczba1 * liczba2            
            elif nadawca.text() == "&Procent":				
                try:
                    wynik = liczba1 / 100 * liczba2
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return
            elif nadawca.text() == "&Potega":
                wynik = liczba1.__pow__(liczba2)
            elif nadawca.text() == "&Odwrotność":
                wynik = 1/liczba1
            elif nadawca.text() == "&Pierwiastek":
                try:
                    wynik = cmath.sqrt(liczba1)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return
            elif nadawca.text() == "&Dziel":
                try:
                    wynik = liczba1 / liczba2
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nigdy cholero nie dziel przez zero!")
                    return
            else:
                pass
            self.wynikEdt.setText(str(wynik))
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())

