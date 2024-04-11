from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

def calcular_salario_homem(idade, regiao, educacao, raca, horas_trabalhadas):
    # Calcula o salário médio com base nos coeficientes obtidos rodando apenas dados para homens
    coef = {
        'intercept': 5.685811,
        'idade': 0.045034,
        'horas_trabalhadas': 0.019579,
        'raca_nao_branca': -0.145173,
        'regiao_Centro-Oeste': 0.140094,
        'regiao_Nordeste': -0.418006,
        'regiao_Norte': -0.206334,
        'regiao_Sul': 0.102244,
        'educ_Ensino Médio': 0.227011,
        'educ_Ensino Superior': 0.814948,
        'educ_Especialização de nível superior, mestrado, doutorado': 1.387907,
        'idade2': -0.000451
    }
    
    idade = int(idade)
    horas_trabalhadas = int(horas_trabalhadas)
    idade2 = idade ** 2
    
    log_salario = coef['intercept']
    log_salario += coef['idade'] * idade + coef['idade2'] * idade2 + coef['horas_trabalhadas'] * horas_trabalhadas
    
    if raca != 'branca':
        log_salario += coef['raca_nao_branca']
    
    if regiao == 'Centro-Oeste':
        log_salario += coef['regiao_Centro-Oeste']
    elif regiao == 'Nordeste':
        log_salario += coef['regiao_Nordeste']
    elif regiao == 'Norte':
        log_salario += coef['regiao_Norte']
    elif regiao == 'Sul':
        log_salario += coef['regiao_Sul']
    
    if educacao == 'Ensino Médio':
        log_salario += coef['educ_Ensino Médio']
    elif educacao == 'Ensino Superior':
        log_salario += coef['educ_Ensino Superior']
    elif educacao in ['Especialização de nível superior', 'mestrado', 'doutorado']:
        log_salario += coef['educ_Especialização de nível superior, mestrado, doutorado']
    
    salario_homem = np.exp(log_salario)
    
    return salario_homem

def calcular_salario_mulher(idade, regiao, educacao, raca, horas_trabalhadas):
    # Calcula o salário médio com base nos coeficientes obtidos rodando apenas dados para mulheres
    coef = {
        'intercept': 5.759549,
        'idade': 0.028889,
        'horas_trabalhadas': 0.024785,
        'raca_nao_branca': -0.163914,
        'regiao_Centro-Oeste': 0.061350,
        'regiao_Nordeste': -0.342485,
        'regiao_Norte': -0.114828,
        'regiao_Sul': 0.057751,
        'educ_Ensino Médio': 0.084512,
        'educ_Ensino Superior': 0.683671,
        'educ_Especialização de nível superior, mestrado, doutorado': 1.186437,
        'idade2': -0.000306
    }
    
    idade = int(idade)
    horas_trabalhadas = int(horas_trabalhadas)
    idade2 = idade ** 2
    
    log_salario = coef['intercept']
    log_salario += coef['idade'] * idade + coef['idade2'] * idade2 + coef['horas_trabalhadas'] * horas_trabalhadas
    
    if raca != 'branca':
        log_salario += coef['raca_nao_branca']
    
    if regiao == 'Centro-Oeste':
        log_salario += coef['regiao_Centro-Oeste']
    elif regiao == 'Nordeste':
        log_salario += coef['regiao_Nordeste']
    elif regiao == 'Norte':
        log_salario += coef['regiao_Norte']
    elif regiao == 'Sul':
        log_salario += coef['regiao_Sul']
    
    if educacao == 'Ensino Médio':
        log_salario += coef['educ_Ensino Médio']
    elif educacao == 'Ensino Superior':
        log_salario += coef['educ_Ensino Superior']
    elif educacao in ['Especialização de nível superior', 'mestrado', 'doutorado']:
        log_salario += coef['educ_Especialização de nível superior, mestrado, doutorado']
    
    salario_mulher = np.exp(log_salario)
    
    return salario_mulher

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dados.html')
def dados():
    return render_template('dados.html')

@app.route('/resultado.html', methods=["GET"])
def resultado():
    idade = request.args.get('idade')
    educacao = request.args.get('educ')
    regiao = request.args.get('regiao')
    raca = request.args.get('raca')
    horas_trabalhadas = request.args.get('hrs_trab')

    salario_estimado_homem = calcular_salario_homem(idade, regiao, educacao, raca, horas_trabalhadas)
    salario_estimado_mulher = calcular_salario_mulher(idade, regiao, educacao, raca, horas_trabalhadas)


    salario_estimado_mulher = f"{float(salario_estimado_mulher):,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
    salario_estimado_homem = f"{float(salario_estimado_homem):,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")

    return render_template('resultado.html', salario_homem=salario_estimado_homem, salario_mulher=salario_estimado_mulher)

if __name__ == '__main__':
    app.run(debug=True)
