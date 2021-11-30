from flask import Flask
from flask_restful import Resource, Api
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


app = Flask(__name__)
api = Api(app)


def fetch_exercise_data_online():
    url = 'https://raw.githubusercontent.com/vitorquintella/API_exercicio/main/get_from_web/BankChurners.csv'
    return pd.read_csv(url)


class Filtro(Resource):
    # https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
    def __init__(self):
        super().__init__()
        self.df = fetch_exercise_data_online()
        self.df = self.df.drop(columns=[
            'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
            'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
        ])
        self.df_groupedby = None

    def get(self, card):
        self.card = card
        df = self._filter_by_card(self.card)
        self._agrupar_marital_status(df)
        self._perpetuar_agrupados()
        self._generate_grouped_plain_plot()
        self._generate_Churn_Education_plot()
        self._generate_corr_plot()

        return f'Tudo ok: Dados do cartao "{self.card}" persistidos no sistema.'

    def _perpetuar_agrupados(self):
        self.df_groupedby.to_csv(f'{self.card}_card_GroupedData.csv')
        self.df_groupedby.to_json(f'{self.card}_card_GroupedData.json')

    def _agrupar_marital_status(self, df):
        self.df_groupedby = df.groupby('Marital_Status').mean()[['Total_Trans_Amt']]

    def _generate_grouped_plain_plot(self):
        plt.figure(figsize=(10, 5))
        plot1 = plt.bar(x=self.df_groupedby.reset_index()['Marital_Status'],
                height=self.df_groupedby.reset_index()['Total_Trans_Amt'])
        plt.title(f'{self.card} card: Gasto agrupado por Total_Trans_Amt')
        plt.savefig(f'{self.card}_card_g1_SimplesGastoAgrupadoPorMaritalStatus.png')
        plt.clf()

    def _generate_Churn_Education_plot(self):
        plt.figure(figsize=(10, 5))
        plot2 = sns.countplot(x=self.df['Education_Level'], hue=self.df['Attrition_Flag'])
        plt.title(f'{self.card} card: Churn por Education Level')
        plt.savefig(f'{self.card}_card_g2_ChurnporEducationLevel.png')
        plt.clf()

    def _generate_corr_plot(self):
        plt.figure(figsize=(10, 8))
        plot3 = sns.heatmap(self.df.corr(), cmap='coolwarm', vmin=-1, vmax=1)
        plt.title(f'{self.card} card: HeatMap de correlação')
        plt.savefig(f'{self.card}_card_g3_HeatMapDeCorrelacao.png')
        plt.clf()


    def _filter_by_card(self, card):
        dado_procurado = self.df['Card_Category'] == card
        df = self.df[dado_procurado]
        return df

class Home(Resource):
    def get(self):
        texto_home = ("Use '/filtro/*ClasseCartao*'  "
                      "Onde *ClasseCartao* eh uma das seguintes opcoes: "
                      "'Blue', 'Gold', 'Silver' ou 'Platinum'")
        return texto_home

api.add_resource(Filtro,  '/filtro/<string:card>')
api.add_resource(Home,'/')


if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app
