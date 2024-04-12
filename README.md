# Desigualdade Salarial entre Gêneros no Brasil
## Trabalho final para o certificado de Jornalismo de Dados e Automação do Master no Insper

Através da base de dados dos quatro trimestres de 2023 da [PNADContínua](https://www.ibge.gov.br/estatisticas/sociais/trabalho/9171-pesquisa-nacional-por-amostra-de-domicilios-continua-mensal.html) disponibilizada pelo IBGE, foi possível calcular regressões lineares, utilizando o método OLS *(ordinary least squares)*. Foi rodado uma regressão para cada gênero: uma utilizando a base de dados filtrada para **mulheres** e outra para **homens**.

A regressão utilizada foi:

A fórmula da regressão linear para o logaritmo do salário por hora (`log_salario_hora`) em função das características dos indivíduos é dada por:

$$
\log(\text{salario\_hora}) = \beta_0 + \beta_1 \cdot \text{idade} + \beta_2 \cdot \text{raca\_nao\_branca} + \beta_3 \cdot \text{regiao\_Norte} + \beta_4 \cdot \text{regiao\_Nordeste} + \beta_5 \cdot \text{regiao\_Sul} + \beta_6 \cdot \text{regiao\_Centro\_Oeste} + \beta_7 \cdot \text{educ\_Fundamental\_I} + \beta_8 \cdot \text{educ\_Fundamental\_II} + \beta_9 \cdot \text{educ\_Medio} + \beta_{10} \cdot \text{educ\_Superior} + \epsilon
$$

onde $\beta_i$ são os coeficientes estimados para cada variável explicativa, e $\epsilon$ é o termo de erro.
