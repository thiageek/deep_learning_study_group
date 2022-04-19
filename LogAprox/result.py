# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:01:12 2022

@author: italo
"""

from keras.models import load_model

import math

model = load_model( 'rna.p5' )

entradas=[]
for x in range( 1, 11 ):
    entradas.append( x )

saidas = model.predict( entradas )

for i in range( 0, len(entradas) ):    
    print( f'log10({entradas[i]})={math.log10(entradas[i])}  <==>  {saidas[i][0]}', end='\n' )
