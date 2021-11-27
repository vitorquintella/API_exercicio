from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json
import requests
import ast

app = Flask(__name__)
api = Api(app)


def fetch_exercise_data_online():
    url = 'https://raw.githubusercontent.com/vitorquintella/API_exercicio/main/get_from_web/BankChurners.csv'
    return pd.read_csv(url)


class Dados(Resource):
    # https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
    def __init__(self):
        super().__init__()
        self.df = fetch_exercise_data_online()

    def get(self, card):
        df = self._filter_by_card(card)
        df = df.head(10)
        print(df)
        return df.to_json()

    def _filter_by_card(self, card):
        dado_procurado = self.df['Card_Category'] == card
        df = self.df[dado_procurado]
        return df


class Graficos(Resource):
    def get(self):
        return "Em construção"

api.add_resource(Dados,  '/<string:card>')  # '/dados' is our entry point for dados
api.add_resource(Graficos, '/graficos')  # '/dados' is our entry point for dados


if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app