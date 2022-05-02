# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:01:12 2022

@author: italo
"""

from keras.models import load_model

import math

model = load_model( 'rna.p5' )

entradas=[ [ 0, 0 ], [ 0, 1 ], [ 1, 0 ], [ 1, 1 ] ]

saidas = model.predict( entradas )

for i in range( 0, len(entradas) ):    
    print( f'{entradas[i][0]} xor {entradas[i][1]} = {saidas[i][0]}', end='\n' )
