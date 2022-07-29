""" 
Analise de dados

Aprender a criar um código de análise de dados.

No dia a dia das empresas, é muito comum dúvidas sobre os resultados da empresa.
Um conceito que cada dia mais cresce nas empresas é o data driven.
Basicamente, é dizer que ações são tomadas com base nos dados e não em achismos.
Com esse desafio pretendo apreender como fazer uma análise utilizando os seguintes conceitos: 

-Importando dados
de bases . csv

-Tratar dados usando
a biblioteca Pandas

-Importação de
bibliotecas

-Criação de gráficos
usando o plotly

Desafio:
Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?

Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing
Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

"""



# Passo 1: Importar a base de dados

import pandas as pd

tabela = pd.read_csv('telecom_users.csv')

# Passo 2: Visualizar a base de dados.
# Entender as informações qie você tem disponivel.
# Descobrir quais problemas existem nessa base de dados.

print(tabela)
print(('\n')*3)

# Excluir colunas inuteis.
# No piton: 
# axis = 0 -> eixo da linha
# axis = 1 -> eixo da coluna

tabela = tabela.drop('Unnamed: 0', axis = 1 )
tabela = tabela.drop('Codigo', axis = 1 )
tabela = tabela.drop('IDCliente', axis = 1 )

print(tabela)
print(('\n')*3)

# Passo 3: Tratamento de Dados (Resolver os problemas da base de dados)
# Informações do tipo corretas= ajustar total gasto.

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors = 'coerce')

# Informações vazias 
# Colunas completamente vazias -> excluir
tabela = tabela.dropna(how = 'all' , axis = 1)

# Linhas que tem alguma informação vazia
tabela = tabela.dropna(how = 'any' , axis = 0)

print(tabela.info())
print(('\n')*3)

# Passo 4: Analise Inicial dos dados

print(tabela['Churn'].value_counts())
print(('\n')*2)
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))
print(('\n')*2)


# Passo 5: Descobrir os motivos do cancelamento. 

import plotly.express as px

for coluna in tabela.columns:
# Graficos se fazem em duas etapas:
# # etapa 1: Cria o grafico.
    grafico = px.histogram(tabela, x= coluna, color= 'Churn', text_auto=True)
    # etapa 2: Exibe o grafico. 
    grafico.show()

#EXEMPLOS DE TIPOS DE GRAFICOS DO PLOTLY = https://plotly.com/python/


#>>>>>>>>>>>>>----ESCREVA AS SUAS CONCLUSÕES----<<<<<<<<<<<<<

# - Clientes que estão a pouco tempo, estão cancelando muito. 
# - Clientes que pagam com boleto eletronico, cancelam mais. 
# - Clientes com contrato mensal, cancelam mais. 
# - Quantos mais serviços tem o cliente cancela menos. 




