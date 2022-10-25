import datetime
import json
from abc import abstractmethod

import requests


class AbstractModel:
    @abstractmethod
    def convert(self, betrag, from_currency, to_currency):
        pass


class LocalCurrencyConverter(AbstractModel):
    file = ""

    def __init__(self):
        pass

    def convert(self, betrag, from_currency, to_currency):
        with open("convert.json") as user_file:
            file_contents = user_file.read()

        parsed_json = json.loads(file_contents)

        ret_str = str(betrag) + " " + from_currency + " entsprechen: \n"
        betragUSD = betrag * parsed_json['data']['USD']['value']
        for i in to_currency:
            ret_str += "\t - " + str(parsed_json['data'][i]['value'] * betragUSD) + " " + parsed_json['data'][i][
                'code'] + " (Kurs: " + str(parsed_json['data'][i]['value'] * parsed_json['data']['USD']['value']) + ")\n "
        ret_str += "Stand: " + str(
            datetime.datetime.strptime(parsed_json['meta']['last_updated_at'], "%Y-%m-%dT%H:%M:%SZ"))
        return ret_str


class RESTCurrencyConverter(AbstractModel):
    url = "https://api.currencyapi.com/v3/latest"
    apikey = "PjdZPf0Blgsc9KjSvFLhGVo1IFTOMOrEFOkSTXi9"

    def __init__(self):
        pass

    def convert(self, betrag, from_currency, to_currency):
        req = requests.get(self.url, params={
            'apikey': self.apikey,
            'base_currency': from_currency,
            'currencies': ",".join(to_currency)
        })
        parsed_json = json.loads(req.content)

        ret_str = str(betrag) + " " + from_currency + " entsprechen: \n"
        for i in to_currency:
            ret_str += "\t - " + str(parsed_json['data'][i]['value'] * betrag) + " " + parsed_json['data'][i][
                'code'] + " (Kurs: " + str(parsed_json['data'][i]['value']) + ")\n "
        ret_str += "Stand: " + str(
            datetime.datetime.strptime(parsed_json['meta']['last_updated_at'], "%Y-%m-%dT%H:%M:%SZ"))
        return ret_str
