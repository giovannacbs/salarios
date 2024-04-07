from flask import Flask, render_template, request
import pymongo
import os
from pymongo import MongoClient

uri = os.environ['mongodb_uri']
db = MongoClient(uri, ssl=True, tlsAllowInvalidCertificates=True)['mjd_2024']
pnad = db.pnad23_gdcbs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    # Obtendo os valores do formulário
    faixa_etaria = request.form['faixa_etaria']
    educ = request.form['educ']
    regiao = request.form['regiao']
    raca = request.form['raca']
    hrs_trab = request.form['hrs_trab']
    ocup = request.form['ocup']

    # Criando o filtro com base nas entradas
    filtro = {
        "faixa_etaria": faixa_etaria,
        "educ": educ,
        "regiao": regiao,
        "raca": raca,
        "hrs_trab": hrs_trab,
        "ocup": ocup
    }

    # Removendo entradas vazias do filtro
    filtro = {k: v for k, v in filtro.items() if v}

    # Agora, realizamos a consulta ao MongoDB
    resultado = pnad.aggregate([
        {"$match": filtro},
        {"$group": {"_id": "$sexo", "media_salario": {"$avg": "$salario"}}}
    ])

    # Preparando a resposta
    salarios = list(resultado)
    resposta = "Média de Salários:<br>"
    for salario in salarios:
        resposta += f"Sexo: {salario['_id']}, Média Salário: {salario['media_salario']}<br>"

    return resposta

if __name__ == '__main__':
    app.run(debug=True)

