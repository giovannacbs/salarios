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

@app.route('/resultado', methods=['POST'])
def resultado():
    print(request.form)
    # Obtendo os valores do formulário
    faixa_etaria = request.form['faixa_etaria']
    educ = request.form['educ']
    regiao = request.form['regiao']
    raca = request.form['raca']
    hrs_trab = request.form['hrs_trab']
    ocup = request.form['ocup']

    # Criando e aplicando o filtro
    filtro = {k: v for k, v in {
        "faixa_etaria": faixa_etaria,
        "educ": educ,
        "regiao": regiao,
        "raca": raca,
        "hrs_trab": hrs_trab,
        "ocup": ocup
    }.items() if v}

    # Consulta ao MongoDB
    medias = pnad.aggregate([
        {"$match": filtro},
        {"$group": {"_id": "$sexo", "media_salario": {"$avg": "$salario"}}}
    ])

    # Passando os resultados para o template
    salarios = list(medias)
    return render_template('resultado.html', salarios=salarios)

if __name__ == '__main__':
    app.run(debug=True)

