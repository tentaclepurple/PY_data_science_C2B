#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 16:01:12 2022

@author: mydoctor
"""

# 1.Crear una función que multiplique 2 números, mediante sumas.  
# Llama a dicha función multiplicación.

def multiplicacion(a, b):
    resultado = 0
    while b > 0:
        resultado += a
        b -= 1
    return resultado


# 2.Crear una función que calcule el cuadrado de un número (entero o no).

def cuadrado(x):
    '''
    x: int o float.
    '''
    return x*x


# 3. Crear una función que devuelva el valor de una ecuación de segundo grado.
# NOTA:  Las ecuaciones de segundo grado se resuelven a partir de:
# a * x2 + b * x + c

def evaluar_cuadratica(a, b, c, x):
    '''
    a, b, c: valores numéricos de los coeficientes de una ecuación
    de segundo grado
    x: valor de la variable x.
    '''
    
    return a*x*x+b*x+c


# 4. Crear una función llamada imprimirNombre que, dado un nombre y apellido,
# los invierta (a menos que se le indique lo contrario).
# Ej:	imprimirNombre (“John”,“Smith”).  La función devolverá Smith John
#		imprimirNombre (“John”,“Smith”, False).  La función devolverá John Smith

def imprimirNombre (nombre, apellido, revertir = True):
    if revertir:
        print(apellido + ', ' + nombre)
    else:
        print(nombre, apellido)


# 5.Desarrolla un función que calcule el máximo comun divisor de 2 números.
# La idea es usar iteración.  El máximo comun divisor, es aquel número que 
# divide a otros 2 y su resto es 0.
# Empezar comprobando la división entre el mayor y el menor número.
# Posteriormente ir reduciendo el menor número en 1 e ir probando la división
# entre el mayor y menor.
# El máximo común divisor, será el mayor número que divida a los 2 con resto = 0

def MCD_iter(a, b):
    '''
    a, b: enteros positivos
    
    devuelve, un entero positivo = máximo comun divisor entre a y b
    '''
    if a > b:
        divisor = b
        dividendo = a
    if b > a:
        divisor = a
        dividendo = b
    if b == a:
        return b
    
    inicio = divisor
    while inicio > 1:
        if dividendo % inicio == 0 and divisor % inicio == 0:
            return inicio
    
        else:
            inicio -= 1
            
            
    return inicio


# 6.Desarrolla una función que calcule la potencia de un número dado, 
# usando la multiplicación. 2^3 = 2 * 2 * 2

def potencia_iter(base, exp):
    '''
    base: entero o coma flotante
    exp: entero >= 0
 
    devuelve: entero o coma flotante -> base^exp
    '''
    if exp <=0:
        return 1
    resultado = base
    for a in range(1,exp):
        resultado = base * resultado
    return resultado


# 7. Desarrollar una función que devuelva la cuota a pagar en un préstamo 
# a un año con un interés anual del 12%.  La cuota dependerá de los 
# intereses a pagar.
# NOTA: 	Interes = Capital * (interes anual / 100) /12
#           Cuota = Capital / 12 + Intereses

def cuota (principal, interes = 12):
    interes = principal * (interes/100) / 12
    cuota = principal / 12 + interes
    return round(cuota, 4)


# 8.Desarrollar una función que calcule si una cadena de texto tiene 
# un numero par o impar de caracteres

def esPar (aStr):
    '''
    aStr: Cadena de texto
     
    devuelve: 1 si es par, 0 si es impar
    '''
    if len(aStr) % 2 == 0:
        tmp = 1
        return tmp        
    else:
        tmp = 0
        return tmp
        
    
# 9.Desarrollar una función que encuentre los números divisibles entre 
# 7 (pero no 5) para todos los números entre 1000 y 2000 (ambos incluidos).

l=[]
for i in range(1000, 2001):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))



