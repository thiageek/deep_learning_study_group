from keras.models import load_model

import numpy as np

model = load_model('model.p5')

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

output = model.predict(np.array(map))

print(output)

for i in range(0,8):
    print(f'Input: {map[i]} | Expected Output: {i} | Output: {output[i][0]}')