# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:50:21 2022

@author: italo
"""

from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import SGD

from keras.losses import MeanSquaredError

from matplotlib import pyplot as plt

import random  

amostras=[ [0,0], [0,1], [1,0], [1,1] ];
saidas=[ [0], [1], [1], [0] ]

rvaux=[]
for i in range( 0, len(amostras) ):
    rvaux.append( i );
        
for i in range( 0, len(amostras) ):
    r = random.randint(0, len(amostras)-i-1 )
    aux = amostras[ i ]
    amostras[ i ] = amostras[ rvaux[ r ] ]
    amostras[ rvaux[ r ] ] = aux
    
    aux2 = saidas[ i ]
    saidas[ i ] = saidas[ rvaux[ r ] ]
    saidas[ rvaux[ r ] ] = aux2
    
    del rvaux[ r ] 
                
model = Sequential()
model.add(Dense(2, activation='sigmoid',input_dim=2))
model.add(Dense(1, activation='sigmoid'))

sgd = SGD(learning_rate=0.5)
model.compile(loss=MeanSquaredError(), optimizer=sgd, metrics=['mse'])

historico=model.fit( amostras, saidas, batch_size=1, epochs=5000 )

model.save( 'rna.p5')      
    
plt.plot(historico.history['mse'])
plt.title('Curvas de erro quadrático médio')
plt.xlabel('Epocas')
plt.ylabel('Erro')
plt.legend(['Erro QM'], loc='upper left')
plt.show()

