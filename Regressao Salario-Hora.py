#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_csv("pnad23.csv", usecols = ["salario", "idade", "raca", "regiao", "educ", "horas_trabalhadas", "sexo"])


# In[51]:


# Limpeza da base
df = df.dropna()
df = df.query("raca != 'Ignorado'")


# In[52]:


# Transformando o salário em salário/hora
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
df['horas_trabalhadas'] = pd.to_numeric(df['horas_trabalhadas'], errors='coerce')
df['salario_hora'] = df['salario'] / df['horas_trabalhadas']


# In[53]:


# Preparando a variável 'raça': 1 se o indivíduo for branco, 0 para todas as outras
df['raca_nao_branca'] = (df['raca'] != 'Branca').astype(int)

# Para 'regiao' e 'educ', criei os dummies manualmente para permitir a especificação das categorias omitidas
# Para 'regiao', omiti 'Sudeste'
regioes = pd.get_dummies(df['regiao'], prefix='regiao')
regioes = regioes.drop('regiao_Sudeste', axis=1)

# Para 'educ', omiti 'Educação Infantil'
educacao = pd.get_dummies(df['educ'], prefix='educ')
educacao = educacao.drop('educ_Educação Infantil', axis=1)


# In[54]:


# Unindo as novas variáveis ao DataFrame, excluindo as colunas originais
df = pd.concat([df, regioes, educacao], axis=1)
df.drop(['raca', 'regiao', 'educ'], axis=1, inplace=True)

# Convertendo 'salario' para o logaritmo de 'salario'
df['log_salario_hora'] = np.log(df['salario_hora'])


# In[55]:


variables = df.columns.drop(['salario','salario_hora' ,'log_salario_hora', 'horas_trabalhadas'])  # Exclui variáveis não explicativas
formula = 'log_salario_hora ~ ' + ' + '.join([f"Q('{var}')" for var in variables])


# In[58]:


# Filtrando o DataFrame para homens
df_homem = df[df['sexo'] == 'Homem']

# Ajustando o modelo de regressão linear para homens
model_homem = smf.ols(formula=formula, data=df_homem).fit()
print("Modelo para Homens:")
print(model_homem.summary())


# In[59]:


# Filtrando o DataFrame para mulheres
df_mulher = df[df['sexo'] == 'Mulher']

# Ajustando o modelo de regressão linear para mulheres
model_mulher = smf.ols(formula=formula, data=df_mulher).fit()
print("\nModelo para Mulheres:")
print(model_mulher.summary())


# In[60]:


# Pegando os coeficientes do modelo para homens
coeficientes_homem = model_homem.params
coeficientes_homem


# In[61]:


# Pegando os coeficientes do modelo para mulheres
coeficientes_mulher = model_mulher.params
coeficientes_mulher


# In[ ]:




