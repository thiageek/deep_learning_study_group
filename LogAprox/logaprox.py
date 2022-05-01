# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:50:21 2022

@author: italo
"""

from keras.models import Sequential
from keras.layers import Dense

from keras.losses import MeanSquaredError

from tensorflow.keras.optimizers import Adam

from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split

import numpy as np  
import random  
import math

amostras = []
for i in range( 0, 50 ):        
    for j in np.arange( 1, 11, 0.01 ):
        if ( j != int( j ) ):
            amostras.append( j )  

rvaux=[]
for i in range( 0, len(amostras) ):
    rvaux.append( i );
        
for i in range( 0, len(amostras) ):
    r = random.randint(0, len(amostras)-i-1 )
    aux = amostras[ i ]
    amostras[ i ] = amostras[ rvaux[ r ] ]
    amostras[ rvaux[ r ] ] = aux
    
    del rvaux[ r ]
    
    
saidas=[]
for i in range( 0, len( amostras ) ):
    saidas.append( math.log10( amostras[i] ) )
    
x_treino, x_teste, y_treino, y_teste=train_test_split(amostras, saidas, test_size=0.2, random_state=42)   
    
model = Sequential()
model.add(Dense(3, activation='selu',input_dim=1))
model.add(Dense(1, activation='selu'))

model.compile(loss=MeanSquaredError(), metrics=['mse'])

historico=model.fit( x_treino, y_treino, validation_data=(x_teste, y_teste), batch_size=10, epochs=10 )

model.save( 'rna.p5')      
    
plt.plot(historico.history['val_mse'])
plt.title('Curvas de erro de validação')
plt.xlabel('Epocas')
plt.ylabel('Val. erro')
plt.legend(['Val. Erro QM'], loc='upper left')
plt.show()


plt.plot(historico.history['mse'])
plt.title('Curvas de erro quadrático médio')
plt.xlabel('Epocas')
plt.ylabel('Erro')
plt.legend(['Erro QM'], loc='upper left')
plt.show()


