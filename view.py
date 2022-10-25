from PyQt6 import uic
from PyQt6.QtWidgets import *


class View(QMainWindow):
    pb_umrechnen: QPushButton
    pb_exit: QPushButton
    pb_reset: QPushButton
    result: QTextBrowser
    currency_select: QListWidget
    betrag: QDoubleSpinBox
    base_currency: QComboBox
    live_data: QCheckBox
    statusbar: QStatusBar
    list_ausgang = ["EUR", "USD", "CHF"]
    list_ziel = ["CAD", "HKD", "ISK", "PHP", "DKK", "HUF",
                 "CZK", "AUD", "RON", "SEK", "IDR",
                 "INR", "BRL", "RUB", "HRK", "JPY",
                 "THB", "CHF", "SGD", "PLN", "BGN", "TRY",
                 "CNY", "NOK", "NZD", "ZAR", "USD", "EUR",
                 "MXN", "ILS", "GBP", "KRW", "MYR"]

    def __init__(self, c):
        super().__init__()
        uic.loadUi("GUI.ui", self)
        for i in self.list_ziel:
            self.currency_select.addItem(i)
        for i in self.list_ausgang:
            self.base_currency.addItem(i)
        self.currency_select.sortItems()
        self.pb_umrechnen.clicked.connect(c.umrechnen)
        self.pb_reset.clicked.connect(c.reset)

    def reset(self):
        self.base_currency.setCurrentIndex(0)
        self.currency_select.setCurrentIndex(0)
        self.result.setText("")
        self.betrag.setValue(None)

    def show_message_status(self, msg: str):
        self.statusbar.showMessage(msg)

    def change_result(self, r):
        self.result.setText(str(r))

    def get_selected_currencies(self):
        selected = self.currency_select.selectedItems()
        ret = []
        for i in selected:
            ret.append(i.text())
        return ret

    def get_selected_currency(self):
        return self.base_currency.currentText()

    def get_value(self):
        return self.betrag.value()

    def get_live(self):
        return self.live_data.isChecked()
