#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:36:22 2024

@author: jacques
"""
import pandas as pd
import matplotlib.pyplot as plt
#pd.set_option('display.max_columns',1000)
#%%
entradas = pd.read_csv('entradas_Parte2 - entradas_Parte2.csv')
saida = pd.read_csv('saidas_Parte2 - saidas_Parte2.csv')
print(entradas.head())
#%%
print(entradas.isnull().sum())

print(saida.isna().sum())
#%%
#OneHotEncoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelEncoder_entradas = LabelEncoder()
entradas.iloc[:,1] = labelEncoder_entradas.fit_transform(entradas.iloc[:,1])
entradas.iloc[:,2] = labelEncoder_entradas.fit_transform(entradas.iloc[:,2])
entradas.iloc[:,5] = labelEncoder_entradas.fit_transform(entradas.iloc[:,5])
entradas.iloc[:,6] = labelEncoder_entradas.fit_transform(entradas.iloc[:,6])
entradas.iloc[:,8] = labelEncoder_entradas.fit_transform(entradas.iloc[:,8])
entradas.iloc[:,10] = labelEncoder_entradas.fit_transform(entradas.iloc[:,10])
entradas.iloc[:,11] = labelEncoder_entradas.fit_transform(entradas.iloc[:,11])
entradas.iloc[:,12] = labelEncoder_entradas.fit_transform(entradas.iloc[:,12])

print(entradas.shape)
#%%
oneHotEnconder = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [1,2,5,6,8,10,11,12])], remainder='passthrough')
entradas = oneHotEnconder.fit_transform(entradas)
print(entradas.shape)
#%%
print(entradas.shape)
#%%
#Separando teste e treinamento
from sklearn.model_selection import train_test_split
#19% para teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(entradas, saida, test_size=0.19)
#%%
print('previsores_treinamento: ' + str(previsores_treinamento.shape))
print('previsores_teste: ' + str(previsores_teste.shape))
print('classe_treinamento: ' + str(classe_treinamento.shape))
print('classe_teste: ' + str(classe_teste.shape))
#%%
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Dense
from keras.regularizers import l2
from keras.layers import BatchNormalization
from keras.initializers import HeNormal
#%%
classificador = Sequential()
classificador.add(Dense(units = 128, input_dim = entradas.shape[1]
                        ,kernel_initializer='random_uniform',kernel_regularizer=l2(0.0001),
                        activation = 'relu'))
classificador.add(BatchNormalization())  # Adicionando Batch Normalization

classificador.add(Dense(units = 64
                        ,kernel_initializer='random_uniform',
                        activation = 'relu'))
#classificador.add(Dropout(0.05))  # Dropout para regularização 

classificador.add(Dense(units = 48
                        ,kernel_initializer='random_uniform',
                        activation = 'relu'))
#classificador.add(Dropout(0.05))  # Dropout para regularização

classificador.add(Dense(units = 1
                        ,kernel_initializer='random_uniform',
                        activation = 'sigmoid'))

#classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy',metrics = ['binary_accuracy'])
from keras.optimizers import AdamW # Import AdamW from Keras

#Compile the model with AdamW optimizer
classificador.compile(optimizer=AdamW(learning_rate=0.00001, weight_decay=1e-4),
                       loss='binary_crossentropy',
                       metrics=['binary_accuracy'])
#%%
#Treinando modelog
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 10, epochs = 800)
#%%
previsoes = classificador.predict(previsores_teste)

import numpy as np
# Convert probabilities to class labels using a threshold (e.g., 0.5)
previsoes = (previsoes > 0.4).astype(int)

# Now, you can use previsoes with accuracy_score and other metrics:
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
acuracia = accuracy_score(classe_teste, previsoes)
precisao = precision_score(classe_teste, previsoes)
recall = recall_score(classe_teste, previsoes)
f1score = f1_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

print('Acurácia: %f' % acuracia)
print('Precision: %f' % precisao)
print('Recall: %f' % recall)
print('F1-Score: %f' % f1score)
print(matriz)

import seaborn as sns
from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(classe_teste, previsoes)
# Visualize a matriz de confusão usando seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(matriz, annot=True, fmt="d", cmap="Blues", cbar=False,linewidths=1.0, linecolor='grey')
plt.xlabel("Classe Prevista",fontweight="bold")
plt.ylabel("Classe Real",fontweight="bold")
plt.title("Matriz de Confusão",fontweight="bold")
plt.show()