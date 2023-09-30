#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:31:00 2022

@author: mydoctor
"""
x = int (input("Introduce un valor entero: "))
cuadrado = 0


for a in range(x):
	cuadrado = cuadrado + x

print (str(x)+ "*" + str(x) + " = " + str(cuadrado))	


x = int (input("Introduce un valor entero: "))
cuadrado = 0
iteraciones_pendientes = x

while iteraciones_pendientes != 0:
    cuadrado = cuadrado + x
    iteraciones_pendientes -= 1
# it
eraciones_pendientes = iteraciones_pendientes - 1
print (str(x)+ "*" + str(x) + " = " + str(cuadrado))