# API_exercicio

* O aplicativo acessa a base de dados pelo link do GITHUB
  * Os dados constam no projeto em /get_from_web/ apenas para manter a organização 

* Uma vez levantada a API, o acesso ao IP puro irá disponibilizar um mini-help


Exemplo de uso:

1 - Executar o main.py

2 - Acessar o IP(O ip gerado pode variar), seguido de /filtro/Gold:

    eg.:  http://127.0.0.1:5000/filtro/Gold

3 - É possível substituir o Gold por:

    'Blue', 'Gold', 'Silver' ou 'Platinum'

4 - Obs.: Base altamente desbalanceada:
```
Contagem de ocorrencias:
Blue        9436
Silver       555
Gold         116
Platinum      20
```


Resposta ao seguinte exercício:
```
Faca um programa que: 
1) Carregue os dados de um csv remoto, ex. csv do github, csv de uma base aberta qualquer ou API.
2) Crie uma api que filtre esses dados e (depois do item 4) retorne o json dos dados filtrados.
3) A partir dos dados filtrados você deve escolher uma variável quantitativa para agregar com um groupby e criar um csv e um json resposta, ambos devem ser persistidos.
4) A partir dos dados filtrados você deve escolher um gráfico para fazer como por exemplo fizemos as gorgetas dadas por sexo ou dia da semana. Crie uma figura png ou jpeg resposta.
5) Coloque sua resposta em um projeto novo no git e envie por e-mail.

```