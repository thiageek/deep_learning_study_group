# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:09:01 2022

@author: italo
"""


from keras.models import Sequential
from keras.layers import Dense

from tensorflow.keras.optimizers import Adam

from keras.losses import MeanSquaredError

from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt

import dadosutil as dsutil

vx, vy = dsutil.geraPontos( 10000 )
vclasses = dsutil.geraClasses( vx, vy )

pontos = dsutil.xyVetsToPontos( vx, vy );
saidas = dsutil.classesToSaidas( vclasses ) 

x_treino, x_teste, y_treino, y_teste=train_test_split(pontos, saidas, test_size=0.2, random_state=42)   
    
model = Sequential()
model.add(Dense(5, activation='selu',input_dim=2))
model.add(Dense(5, activation='selu'))
model.add(Dense(9, activation='softmax'))

optimizer=Adam()
model.compile(loss=MeanSquaredError(), optimizer=optimizer, metrics=['mse'])

historico=model.fit( x_treino, y_treino, validation_data=(x_teste, y_teste), batch_size=64, epochs=500 )

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
