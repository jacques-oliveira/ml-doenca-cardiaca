#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:36:22 2024

@author: jacques
"""
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',1000)
#%%
entradas = pd.read_csv('entradas_Parte2 - entradas_Parte2.csv')
saida = pd.read_csv('saidas_Parte2 - saidas_Parte2.csv')
print(entradas.head())
#%%
print(entradas.isnull().sum())

print(saida.isna().sum())
#%%
#Separando teste e treinamento
from sklearn.model_selection import train_test_split
#19% para teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(entradas, saida, test_size=0.19)
#%%
#Normalizando
from sklearn.preprocessing import MinMaxScaler
#%%
# 1. Crie um objeto MinMaxScaler
scaler = MinMaxScaler()

# 2. Ajuste o scaler aos seus dados de treinamento (previsores_treinamento)
scaler.fit(previsores_treinamento)

# 3. Transforme os dados de treinamento e teste usando o scaler ajustado
previsores_treinamento_normalizados = scaler.transform(previsores_treinamento)
previsores_teste_normalizados = scaler.transform(previsores_teste)
#%%
print(entradas.shape)
#%%
import keras
from keras.models import Sequential
from keras.layers import Dense

classificador = Sequential()
classificador.add(Dense(units = 64, input_dim = 13
                        ,kernel_initializer='random_uniform',
                        activation = 'relu'))

classificador.add(Dense(units = 32
                        ,kernel_initializer='random_uniform',
                        activation = 'relu'))

classificador.add(Dense(units = 16
                        ,kernel_initializer='random_uniform',
                        activation = 'relu'))

classificador.add(Dense(units = 1
                        ,kernel_initializer='random_uniform',
                        activation = 'sigmoid'))
#%%
#classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy',metrics = ['binary_accuracy'])
from keras.optimizers import AdamW # Import AdamW from Keras

# Compile the model with AdamW optimizer
classificador.compile(optimizer=AdamW(learning_rate=1e-3, weight_decay=1e-4),
                      loss='binary_crossentropy',
                      metrics=['binary_accuracy'])
#%%
#Treinando modelo
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 10, epochs = 5000)