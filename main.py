from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json
import requests
import ast

app = Flask(__name__)
api = Api(app)


class Dados(Resource):
    def get(self):
        df = self._get_data()
        df = df.to_dict()  # convert dataframe to dictionary
        return {'data': df}, 10  # return data and 200 OK code

    def _get_data(self):
        url = 'https://raw.githubusercontent.com/vitorquintella/API_exercicio/main/get_from_web/BankChurners.csv'
        return pd.read_csv(url, delimiter=";")

class Graficos(Resource):
    def get(self):
        return "Em construção"

api.add_resource(Dados, '/dados')  # '/dados' is our entry point for dados
api.add_resource(Graficos, '/graficos')  # '/dados' is our entry point for dados


if __name__ == '__main__':
    app.run()  # run our Flask app