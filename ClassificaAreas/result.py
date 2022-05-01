# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:01:12 2022

@author: italo
"""

from keras.models import load_model

import dadosutil as dsutil

#model = load_model( 'rna.p5' )
model = load_model( 'rna_momentum.p5' )

vx, vy = dsutil.geraPontos( 10000 )
pontos = dsutil.xyVetsToPontos( vx, vy );

saidas = model.predict( pontos )

vclasses = dsutil.saidasToClasses( saidas )

dsutil.plotaDados( vx, vy, vclasses )
