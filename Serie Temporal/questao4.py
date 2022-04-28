import numpy as np
import pandas as pd
from keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import  r2_score

def _ts_function(n):
  equation = np.power(np.sin(n),2) + np.cos(n + np.cos(n))
  return equation

def build_samples(n = 1000):
  X = []
  y = []
  for i in range(n):
    aux_x = []
    aux_y = []
    for x_value in range(i- 10,i,):
      aux_x.append(_ts_function(x_value))
    X.append(aux_x)
    for y_value in range(i + 1, i + 4):
      aux_y.append(_ts_function(y_value))
    y.append(aux_y)
  return X,y

def plot_model(history: pd.DataFrame):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.legend()

def get_metrics(model, X_test:np.array, y_test:np.array):
  yhat = model.predict(X_test)
  r2 = r2_score(y_test, yhat)
  print(f'O resultado desse modelo considerando o R2 Score é de {r2}')

def build_nn(X:list,y:list):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
  model = Sequential()
  model.add(Dense(units = 10, input_shape = (10,), activation = 'tanh'))
  model.add(Dense(units = 8,  activation = 'tanh'))
  model.add(Dense(units = 5,  activation = 'tanh'))
  model.add(Dense(units = 3, activation = 'tanh'))
  model.compile(optimizer = 'nadam', loss='mean_squared_error', metrics=['mean_squared_error',])
  history = model.fit(x=X_train, y=y_train, validation_data = (X_test,y_test), batch_size=16, epochs=100, verbose=2)
  plot_model(history)
  get_metrics(model, X_test, y_test)
  return model

X, y = build_samples()
model = build_nn(X,y)
model.save("ts.p5")