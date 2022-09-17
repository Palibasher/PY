import json
import requests
from config import *


class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(
                f'Нельзя перевести одинаковые валюты {base}.')
        try:
            print(quote)
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {quote}')
        try:
            print(base)
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {base}')
        try:
            amount = int(amount)
        except ValueError:
            raise ExchangeException(f'Не смог обработать количество {amount}')
        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])
        print(r.text)
        print(base_ticker, quote_ticker)
        return total_base
