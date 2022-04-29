# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:59:05 2022

@author: italo
"""

import random
import math
import time

import matplotlib.pyplot as plt 

from matplotlib import colors

def geraPontos( n ):
    vx = []
    vy = []

    random.seed( time.time() )

    for i in range( 0, n ):
        r = random.uniform( 0, 1 );
        theta = random.uniform( -math.pi, math.pi )
        
        x = r * math.cos( theta )
        y = r * math.sin( theta )
        
        vx.append( x )
        vy.append( y )
    
    return vx, vy;
        
        
def geraClasses( vx, vy ):
    vclasses = []

    for i in range( 0, len( vx ) ):        
        x = vx[ i ]
        y = vy[ i ]
        
        classe = 0
        if ( x < 0 ):
            if ( y > 0 ):
                c = x - y + 1
                if ( c > 0 ):
                    classe = 2
                elif ( c < 0 ):
                    classe = 6
            elif ( y < 0 ):
                c = x + y + 1
                if ( c > 0 ):
                    classe = 3
                elif ( c < 0 ):
                    classe = 7
        elif ( x > 0 ):
            if ( y > 0 ):
                c = 1 - x - y
                if ( c > 0 ):
                    classe = 1
                elif ( c < 0 ):
                    classe = 5
            elif ( y < 0 ):
                c = y - x + 1
                if ( c > 0 ):
                    classe = 4
                elif ( c < 0 ):
                    classe = 8
                  
        vclasses.append( classe )
        
    return vclasses
    

def pontosToXYVets( pontos ):
    vx = [];
    vy = [];
    for i in range( 0, len(pontos) ):
        vx.append( pontos[ i ][ 0 ] )
        vy.append( pontos[ i ][ 1 ] )
        
    return (vx, vy)

def xyVetsToPontos( vx, vy ):
    pontos = []
    for i in range( 0, len( vx ) ):
        pontos.append( [ vx[i], vy[ i ] ] )
    return pontos;
    

def classeToSaida( classeI ):
    saida = []
    for i in range( 0, 9 ):
        if ( i == classeI ):
            saida.append( 1 )
        else: 
            saida.append( 0 )
    return saida        

def saidaToClasse( saida ):    
    for i in range( 0, 9 ):
        if ( round( saida[i] ) > 0.5 ):
            return i;
    return 0; 
            
def classesToSaidas( vclasses ):
    saidas = []
    for i in range( 0, len(vclasses) ):
        saidas.append( classeToSaida( vclasses[ i ] ) )
    return saidas;

def saidasToClasses( saidas ):
    vclasses = []
    for i in range( 0, len(saidas) ):
        vclasses.append( saidaToClasse( saidas[ i ] ) )
    return vclasses;


def classes( vclasses ):
    classes = [ 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8' ]
    
    vet = []
    for i in range( 0, len( vclasses ) ):
        vet.append( classes[ vclasses[ i ] ] )    
    return vet;

def plotaDados( vx, vy, vclasses ):            
    fig, ax = plt.subplots()    
        
    circle = plt.Circle((0,0), 1, color='k', fill=False)
    ax.add_patch( circle )
    
    plt.plot( [ -1, 0, 1 ], [ 0, 0, 0 ], color='k' )
    plt.plot( [  0, 0, 0 ], [ -1, 0, 1 ], color='k' )
    plt.plot( [ -1, -0.5, 0 ], [ 0, 0.5, 1 ], color='k' )
    plt.plot( [ -1, -0.5, 0 ], [ 0, -0.5, -1 ], color='k' )
    plt.plot( [ 0, 0.5, 1 ], [ 1, 0.5, 0 ], color='k' )
    plt.plot( [ 0, 0.5, 1 ], [ -1, -0.5, 0 ], color='k' )
    
    vcores = cores( vclasses )
    
    plt.scatter( vx, vy, s=20, marker='o', c=vcores )
    
    plt.show()
            

def cores( vclasses ):
    cores = [ 
        colors.to_rgb('black'), 
        colors.to_rgb('blue'),
        colors.to_rgb('red'),
        colors.to_rgb('green'),
        colors.to_rgb('yellow'),
        colors.to_rgb('cyan'),
        colors.to_rgb('maroon'),
        colors.to_rgb('magenta'),
        colors.to_rgb('orange') ]
    
    vcores = []
    for i in range( 0, len( vclasses ) ):
        vcores.append( cores[ vclasses[ i ] ] )    
    return vcores;            