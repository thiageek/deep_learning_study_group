# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:02:18 2022

@author: italo
"""

from sklearn import metrics

from keras.models import load_model

import dadosutil as dsutil

model = load_model( 'rna.p5' )

vx, vy = dsutil.geraPontos( 1000 )
vclasses = dsutil.geraClasses( vx, vy )

pontos = dsutil.xyVetsToPontos( vx, vy )

saidasObtidas = model.predict( pontos )

vclassesPreditas = dsutil.saidasToClasses( saidasObtidas )

cMat = metrics.confusion_matrix( vclasses, vclassesPreditas )

print( cMat )