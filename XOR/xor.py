# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:50:21 2022

@author: italo
"""

from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import SGD

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
model.compile(loss="binary_crossentropy", optimizer=sgd, metrics=['accuracy'])

historico=model.fit( amostras, saidas, batch_size=1, epochs=2500 )

model.save( 'rna.p5')      
    
plt.plot(historico.history['loss'])
plt.title('Curvas de precisão')
plt.xlabel('Epocas')
plt.ylabel('Precisão')
plt.legend(['validação'], loc='upper right')
plt.show()

