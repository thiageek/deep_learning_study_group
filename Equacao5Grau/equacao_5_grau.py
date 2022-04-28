import numpy as np
import pandas as pd
from keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import  r2_score
def equation(n):
  equation = (10 * np.power(n,5)) + (5 * np.power(n,4)) + (2 * np.power(n,3)) - (0.5 * np.power(n,2)) + (3 * n) + 2 
  return equation
def generate_samples(end,interval = 0.03):
  samples = np.arange(0,end,interval)
  amostras = []
  for i in range( 0, end ):        
    for j in np.arange( 1, 20, 0.03):
        amostras.append( j )
  labels = []
  for i in range(len(amostras)):
      labels.append(equation(amostras[i]))
  return amostras, labels

def plot_model(historico: pd.DataFrame):
    plt.plot(historico.history['val_loss'], label='val_loss')
    plt.plot(historico.history['loss'], label='loss')
    plt.legend()
    plt.show()
def evaluate_model(model, X_test, y_test):
    yhat = model.predict(X_test)
    r2 = r2_score(y_test, yhat)
    plt.plot(yhat, label='results', )
    plt.plot(y_test, label='exact curve',alpha = 0.4)
    plt.legend()
    print(f"O resultado desse modelo considerando o R2 Score é de {r2}")
def build_nn(X,y):
    X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.25, random_state=42)   
    model = Sequential()
    model.add(Dense(units = 15, input_shape = (1,), activation = 'selu',))

    model.add(Dense(units = 12,  activation = 'selu',))
    model.add(Dense(units = 6,  activation = 'selu',))

    model.add(Dense(units = 1, activation = 'selu'))
    model.compile(optimizer = 'adamax', loss='mse', metrics=['mse','accuracy'])
    historico = model.fit(x=X_train, y=y_train, validation_data = (X_test,y_test), batch_size=10, epochs=1000, verbose=2)
    evaluate_model(model,X_test,y_test)
    plot_model(historico)
    return model 
X,y  = generate_samples(50)
build_nn(X,y)
