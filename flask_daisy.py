# -*- coding: utf-8 -*-
"""
    flask_daisy
    ~~~~
    Adds DaisySMS support to Flask applications
"""
import requests


__version__ = '1.0'
__versionfull__ = __version__


class DaisySMS:
    app = None
    api_key = None
    client = None
    default_from = None
    API_HANDLER = "https://daisysms.com/stubs/handler_api.php?"

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.api_key = app.config['DAISYSMS_API_KEY']
    
    def get_balance(self):
        response = requests.get(
            self.API_HANDLER + f"api_key={self.api_key}&action=getBalance"
        )

        return response.json()

    def get_number(self, service, max_price):
        response = requests.get(
            self.API_HANDLER + f"api_key={self.api_key}&action=getNumber&service={service}&max_price={max_price}"
        )

        return response.json()

    def get_status(self, number_id):
        response = requests.get(
            self.API_HANDLER + f"api_key={self.api_key}&action=getStatus&id={number_id}"
        )

        return response.json()

    def set_status(self, number_id, status):
        response = requests.get(
            self.API_HANDLER + f"api_key={self.api_key}&action=setStatus&id={number_id}&status={status}"
        )

        return response.json()
    
    def mark_done(self, number_id):
        return self.set_status(number_id, 6)

    def cancel_rental(self, number_id):
        return self.set_status(number_id, 8)

    def get_prices_verification(self):
        response = requests.get(
            self.API_HANDLER + f"api_key={self.api_key}&action=getPricesVerification"
        )

        return response.json()

    def get_prices(self):
        response = requests.get(
            self.API_HANDLER + f"api_key={self.api_key}&action=getPrices"
        )

        return response.json()
