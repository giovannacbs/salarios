#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
df = pd.read_csv("pnad23.csv", usecols = ["salario", "idade", "raca", "regiao", "educ", "horas_trabalhadas", "sexo"])

# Suponha que 'df' é seu DataFrame pandas já carregado com os dados.
df = df.query('educ != "Educação Infantil"')

# Preparando a variável 'raça': 1 se o indivíduo for branco, 0 para todas as outras
df['raca_nao_branca'] = (df['raca'] != 'Branca').astype(int)

# Para 'regiao' e 'educ', criamos dummies manualmente para permitir a especificação das categorias omitidas
# Para 'regiao', omitimos 'Sudeste'
regioes = pd.get_dummies(df['regiao'], prefix='regiao')
regioes = regioes.drop('regiao_Sudeste', axis=1)

# Para 'educ', omitimos 'Educação Infantil'
educacao = pd.get_dummies(df['educ'], prefix='educ')
educacao = educacao.drop('educ_Ensino Fundamental', axis=1)

# Unindo as novas variáveis ao DataFrame, excluindo as colunas originais
df = pd.concat([df, regioes, educacao], axis=1)
df.drop(['raca', 'regiao', 'educ'], axis=1, inplace=True)

# Convertendo 'salario' para o logaritmo de 'salario'
df['log_salario'] = np.log(df['salario'])

# Criando a variável 'idade2' para idade ao quadrado
df['idade2'] = df['idade'] ** 2

# Suponha que todas as outras etapas de preparação dos dados sejam mantidas conforme descrito anteriormente.

# Vamos garantir que todos os nomes de variáveis são tratados corretamente.
variables = df.columns.drop(['salario', 'log_salario'])  # Exclui variáveis não explicativas
formula = 'log_salario ~ ' + ' + '.join([f"Q('{var}')" for var in variables])

# Filtrando o DataFrame para homens
df_homem = df[df['sexo'] == 'Homem']

# Ajustando o modelo de regressão linear para homens
model_homem = smf.ols(formula=formula, data=df_homem).fit()
print("Modelo para Homens:")
print(model_homem.summary())

# Filtrando o DataFrame para mulheres
df_mulher = df[df['sexo'] == 'Mulher']

# Ajustando o modelo de regressão linear para mulheres
model_mulher = smf.ols(formula=formula, data=df_mulher).fit()
print("\nModelo para Mulheres:")
print(model_mulher.summary())


# In[15]:


coeficientes_homem = model_homem.params
coeficientes_homem


# In[16]:


coeficientes_mulher = model_mulher.params
coeficientes_mulher


# In[ ]:




