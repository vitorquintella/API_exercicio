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
    return pd.read_csv(url, delimiter=";")


class Dados(Resource):
    def __init__(self):
        super().__init__()
        self.df = fetch_exercise_data_online()

    def get(self):
        # df_dict = self.df.head().to_dict()
        df_dict = self.df.to_dict()
        return {'data': df_dict}


class Graficos(Resource):
    def get(self):
        return "Em construção"

api.add_resource(Dados, '/dados')  # '/dados' is our entry point for dados
api.add_resource(Graficos, '/graficos')  # '/dados' is our entry point for dados


if __name__ == '__main__':
    app.run()  # run our Flask app