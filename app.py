from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

def calcular_salario_homem(idade, regiao, educacao, raca, horas_trabalhadas):
    # Calcula o salário médio com base nos coeficientes obtidos rodando apenas dados para homens
    coef = {
    'intercept': 2.887422,
    'idade': 0.011503,
    'raca_nao_branca': -0.113520,
    'regiao_Centro-Oeste': 0.138047,
    'regiao_Nordeste': -0.352450,
    'regiao_Norte': -0.165508,
    'regiao_Sul': 0.112369,
    'educ_Ensino Fundamental': 0.344153,
    'educ_Ensino Médio': 0.657032,
    'educ_Ensino Superior': 1.264284,
    'educ_Especialização de nível superior, mestrado, doutorado': 1.842134}

    idade = int(idade)
    horas_trabalhadas = int(horas_trabalhadas)
    
    log_salario = coef['intercept']
    log_salario += coef['idade'] * idade 
    
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
    
    salario_homem = (np.exp(log_salario))*horas_trabalhadas
    
    return salario_homem

def calcular_salario_mulher(idade, regiao, educacao, raca, horas_trabalhadas):
    # Calcula o salário médio com base nos coeficientes obtidos rodando apenas dados para mulheres

    coef = {
    'intercept': 2.862371,
    'idade': 0.009029,
    'raca_nao_branca': -0.117553,
    'regiao_Centro-Oeste': 0.049813,
    'regiao_Nordeste': -0.309326,
    'regiao_Norte': -0.117362,
    'regiao_Sul': 0.071118,
    'educ_Ensino Fundamental': 0.288476,
    'educ_Ensino Médio': 0.585126,
    'educ_Ensino Superior': 1.173033,
    'educ_Especialização de nível superior, mestrado, doutorado': 1.669707}

    idade = int(idade)
    horas_trabalhadas = int(horas_trabalhadas)
    
    
    log_salario = coef['intercept']
    log_salario += coef['idade'] * idade 
    
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
    
    salario_mulher = (np.exp(log_salario))*horas_trabalhadas
    
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


    salario_estimado_mulher_txt = f"{float(salario_estimado_mulher):,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
    salario_estimado_homem_txt = f"{float(salario_estimado_homem):,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")

    if raca == "Branca":
        raca_txt = "branca"
    else:
        raca_txt = "não branca"

    dados_usuario = f"{idade} anos, de raça {raca_txt}, com estudo até {educacao}, na região {regiao}, trabalhando por {horas_trabalhadas} horas."
    
    percentual =  ((salario_estimado_homem/salario_estimado_mulher)-1)*100

    return render_template('resultado.html', 
                           salario_homem=salario_estimado_homem, 
                           salario_mulher=salario_estimado_mulher, 
                           texto_homem=salario_estimado_homem_txt, 
                           texto_mulher=salario_estimado_mulher_txt,
                           dados_usuario = dados_usuario,
                           percentual = percentual)

if __name__ == '__main__':
    app.run(debug=True)
