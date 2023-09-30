#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 10:45:55 2022

@author: mydoctor
"""
# 1. Crea las siguientes tuplas:
# tupla1 = (1,2,"tres","cuatro",5)
# tupla2 = (1)
tupla1 = (1,2,"tres","cuatro",5)
tupla2 = (1)

# 2.Comprueba el tipo de tupla1 y tupla2.  ¿Es correcto?.  Haz los cambios necesarios en tupla2 para que su tipo sea tupla.
type(tupla1)
type(tupla2)
tupla2 = (1,)
type(tupla2)

# 3.Extrae las posiciones 1 y 2 de tupla1.  
# Extrae las posiciones 2 y 3 de tupla1. 
# Extrae los elementos desde la segunda posición hasta la anteúltima de tupla1. 
# Extrae todos los elementos a partir de la segunda posición de tupla1.
tupla1 [:2]
tupla1 [1:3]
tupla1 [2:-1]
tupla1 [1:]

# 4.Comprueba la longitud de tupla1
len(tupla1)

# 5.Concatena tupla1 y tupla2, guarda el resultado en tupla3.  Comprueba el tamaño de tupla3
tupla3 = tupla1 + tupla2
len (tupla3)

# 6.Duplica tupla1 y guarda el resultado en tupla4.
tupla4 = 2 * tupla1

# 7. Comprueba la existencia o no de los siguientes elementos en tupla1:
# “tres”, “tre”, 4, “cinco”
'tres' in tupla1
'tre' in tupla1
4 in tupla1
'cinco' in tupla1
