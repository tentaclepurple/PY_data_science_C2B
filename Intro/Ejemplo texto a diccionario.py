#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 10:32:45 2022

@author: mydoctor
"""
            
quijote =  open('quijote.txt', 'r')
contenido = quijote.read()
lista_palabras = contenido.split()

               
def tabla_frecuencias (texto):
	diccionario = {}
	for palabra in texto:
		if palabra in diccionario:
			diccionario [palabra] += 1
		else:
			diccionario [palabra] = 1
	return diccionario


resultado = tabla_frecuencias(lista_palabras)
