from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json
import requests
import ast

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        url = 'https://raw.githubusercontent.com/vitorquintella/API_exercicio/main/get_from_web/BankChurners.csv'
        data = pd.read_csv(url,delimiter=";")
        # data = pd.read_csv('users.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 10  # return data and 200 OK code



class Locations(Resource):
    # methods go here
    pass


api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()  # run our Flask app