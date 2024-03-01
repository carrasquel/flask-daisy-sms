# -*- coding: utf-8 -*-
"""
    flask_daisy
    ~~~~
    Adds DaisySMS support to Flask applications
"""


__version__ = '1.0'
__versionfull__ = __version__


class DaisySMS:
    app = None
    api_key = None
    client = None
    default_from = None

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.api_key = app.config['DAISYSMS_API_KEY']
    
    def get_balance(self):
        pass

    def get_number(self, service, max_price):
        pass

    def get_status(self, number_id):
        pass

    def set_status(self, number_id, status):
        pass
    
    def mark_done(self, number_id):        
        pass

    def cancel_rental(self, number_id):
        pass

    def get_prices_verification(self):
        pass

    def get_prices(self):
        pass

