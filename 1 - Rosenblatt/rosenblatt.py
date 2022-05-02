from random import uniform

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense
from keras.losses import MeanSquaredError

from matplotlib import pyplot as plt

import numpy as np

input = []
output = []

map = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]

for i in range(0,8):
    for j in range(0,2001):
        a = map[i][0]+uniform(-0.1,0.1)
        b = map[i][1]+uniform(-0.1,0.1)
        c = map[i][2]+uniform(-0.1,0.1)
        input.append([a,b,c])
        output.append(i)

input = np.array(input)
output = np.array(output)

input, output = shuffle(input, output, random_state=0)

x_train, x_test, y_train, y_test = train_test_split(input, output, test_size=0.2, random_state=7)

model = Sequential()
model.add(Dense(1, activation="relu", input_dim=3))
# model.add(Dense(1, activation="relu"))

model.compile(loss=MeanSquaredError(), metrics=['mse'])

result = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=100)

model.save('model.p5')

plt.plot(result.history['val_mse'])
plt.title('Curva de erro quadrático médio')
plt.xlabel('Epocas')
plt.ylabel('Erro médio')
plt.legend(['validação'], loc='upper left')
plt.show()
