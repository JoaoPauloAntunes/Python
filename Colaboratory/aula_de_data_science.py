# -*- coding: utf-8 -*-
"""Aula de Data Science

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vwETlC0e8d0rWS_27MEr8reSlHGpAIH5
"""

# https://www.youtube.com/watch?v=F608hzn_ygo

import pandas as pd # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

#u ri: Uniform Resource Identifier
uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv' 
filmes = pd.read_csv(uri) # obtém dataframe pegando o arquivo de dado csv no uri e transformando em informação útil 
filmes.head() # este método serve para pegar apenas os primeiros registros deste dataframe 
filmes.columns = ['filmeId', 'titulo', 'generos'] # para lista correspondente aos nomes de colunas, atribui o nome em português 
filmes.head()

uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv'
notas = pd.read_csv(uri)
notas.head()

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.head()

notas["nota"].head() # série; sequência numérica

notas['nota'].unique() # notas -> (0, 5)

notas['nota'].mean() # média

notas['nota'].min() # nota mínima

notas.describe()