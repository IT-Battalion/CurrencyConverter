from model import RESTCurrencyConverter, LocalCurrencyConverter, AbstractModel
from view import View


class Controller:
    def __init__(self):
        self.model = None
        self.view = View(self)
        self.view.show()

    def umrechnen(self):
        live = self.view.get_live()
        if live:
            self.model = RESTCurrencyConverter()
        else:
            self.model = LocalCurrencyConverter()

        if self.model is None:
            self.view.show_message_status("Error: No Model")
        else:
            betrag = self.view.get_value()
            base_currency = self.view.get_selected_currency()
            to_currency = self.view.get_selected_currencies()
            res = self.model.convert(betrag, base_currency, to_currency)
            self.view.change_result(res)
            self.view.show_message_status("Abfrage Success")

    def reset(self):
        self.view.reset()
        self.view.show_message_status("Resetted")

