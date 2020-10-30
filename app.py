# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from service.db.csv_loader import CsvLoader
from service.db.json_loader import JsonLoader
from service.db.fake_loader import FakeLoader
from view.customer import CustomerResource


BASE_PATH = '/juntos'

def config_routes(app):
    api = Api(app)
    api.add_resource(CustomerResource, f'{BASE_PATH}/customer', methods=['GET'], endpoint='get_customer')


APP = Flask(__name__)
config_routes(APP)
# --- Depois de carregar os dados, habilita a API para responder requisições: ---------------
CsvLoader('https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv')
JsonLoader('https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json')

APP.config['available'] = True
# --------------------------------------------------------------------------------------------

if __name__ == '__main__':
    APP.run(debug=True)
