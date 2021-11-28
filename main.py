from flask import Flask
from flask_restful import Resource, Api
import pandas as pd
import matplotlib.pyplot as plt

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
        self.df_groupedby = None

    def get(self, card):
        df = self._filter_by_card(card)
        self._agrupar_marital_status(df)
        self._perpetuar_agrupados()
        self._generate_plot()

        return self.df_groupedby.to_json()

    def _perpetuar_agrupados(self):
        self.df_groupedby.to_csv('grouped_data.csv')

    def _agrupar_marital_status(self, df):
        self.df_groupedby = df.groupby('Marital_Status').mean()[['Credit_Limit']]

    def _generate_plot(self):
        plt.bar(x=self.df_groupedby.reset_index()['Marital_Status'],
                height=self.df_groupedby.reset_index()['Credit_Limit'])
        plt.title("Plot generated using Matplotlib")
        plt.savefig("Grouped_plot.png")

    def _filter_by_card(self, card):
        dado_procurado = self.df['Card_Category'] == card
        df = self.df[dado_procurado]
        return df


api.add_resource(Dados,  '/<string:card>')  # '/dados' is our entry point for dados
# http://127.0.0.1:5000/Blue


if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app
