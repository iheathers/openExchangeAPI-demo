import requests
from cachetools import cached, TTLCache


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(f'{self.BASE_URL}latest.json?app_id={self.app_id}').json()

    def convert(self, from_amount, from_currency, to_currency):
        exchange_rates = self.latest['rates']
        to_rate = exchange_rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / exchange_rates[from_currency]
            return from_in_usd * to_rate

# response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
# exchange_rates = response.json().get('rates')
# ENDPOINT = "https://openexchangerates.org/api/latest.json"
