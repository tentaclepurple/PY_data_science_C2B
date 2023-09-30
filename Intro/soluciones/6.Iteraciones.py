#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 15:31:38 2022

@author: mydoctor
"""

# 1.Crear un programa que imprima una secuencia de números pares, que 
# empezando por el 0, su número más alto sea menor que 30

for a in range(0,30,2):
    print (a)


# 2.Supongamos el siguiente programa:      
iteracion = 0
contador = 0
while iteracion < 5:
    # la variable letra en el loop, itera sobre todos los caracteres
    # de la cadena, incluidas comas, espacios y símbolos
    
    for letra in "¡Hola mundo!": 
        contador += 1
    print("Iteración " + str(iteracion) + "; contador es: " + str(contador))
    iteracion += 1 

# Sin ejecutar el código en Python, analiza el código y responde a las cuestiones.
# 1) ¿Cuál es el valor de la variable contador durante la iteración 0? 12
# 2) ¿Cuál es el valor de la variable contador durante la iteración 1? 24
# 3) ¿Cuál es el valor de la variable contador durante la iteración 2? 36
# 4) ¿Cuál es el valor de la variable contador durante la iteración 3? 48
# 5) ¿Cuál es el valor de la variable contador durante la iteración 4? 60


# 3.Supongamos el siguiente programa:
iteracion = 0
while iteracion < 5:
    contador = 0
    for letra in "¡Hola mundo!":
        contador += 1
    print("Iteracion " + str(iteracion) + "; contador es: " + str(contador))
    iteracion += 1 

# 1) ¿Cuál es el valor de la variable contador durante la iteración 0? 12
# 2) ¿Cuál es el valor de la variable contador durante la iteración 1? 12
# 3) ¿Cuál es el valor de la variable contador durante la iteración 2? 12
# 4) ¿Cuál es el valor de la variable contador durante la iteración 3? 12
# 5) ¿Cuál es el valor de la variable contador durante la iteración 4? 12


# 4.Supongamos el siguiente programa:
iteracion = 0
while iteracion < 5:
    contador = 0
    for letra in "¡Hola mundo!":
        contador += 1
        if iteracion % 2 == 0:
            break
    print("Iteracion " + str(iteracion) + "; contador es: " + str(contador))
    iteracion += 1 

# 1) ¿Cuántas veces se ejecuta el comando print? 5
# 2) ¿Cuál es el máximo valor que toma la variable iteracion? 5
# 3) ¿Cuál es el máximo valor de la variable contador? 12
# 4) ¿Cuál es el menor valor de la variable contador? 1


# 5.Crear un programa que tras introducir un número, nos diga si dicho número 
# tiene cubo perfecto o no.
# Nota: 8 cubo perfecto de 2, 27 cubo perfecto de 3, 64 cubo perfecto de 4, …
x = int(input('Introduce un número entero: '))
x = 27
contador = 0
while contador**3 < x:
    contador = contador + 1
    print(contador)
if contador**3 != x:
    print(str(x) + ' no es un cubo perfecto')
else:
    print('El cubo de ' + str(x) + ' es ' + str(contador))
 
x = 27
for a in range(x+1):
    if a**3 == x:
        print ("cubo perfecto")
        break
else:
    print("no cubo")
    
# 6. Crea un programa que añada elementos a una lista de manera indefinida, 
# mientras pulsemos una tecla
lineas = list()
respuesta = input('Pulsa s si quieres añadir más líneas: ')
while respuesta == 's':
    nueva_linea = input('Siguiente línea: ')
    lineas.append(nueva_linea)
    respuesta = input('Pulsa s si quieres añadir más líneas: ')

print('Las líneas que has introducido son:')
for a in lineas:
    print(a)


# 7. Crea un programa que calcule el factorial de un número.
# Nota: 	Factorial de 4 = 4! = 4 * 3 * 2 * 1
#           Factorial de 5 = 5! = 5 * 4 * 3 * 2 * 1

numero = int(input("Introduce un número: "))
contador = numero
factorial = 1
while contador > 0:
    factorial *= numero
    contador -=1
    numero -= 1
       
print (factorial)


# 8.Crear un programa que extráiga el total de vocales existentes en una 
# cadena de texto.
# NOTA: El programa nos pedirá introducir una cadena de texto y nos 
# devolverá el total de vocales.  Para simplificar la resolución del 
# ejercicio, asegúrate de convertir la cadena de texto a analizar a minúsculas.

cadena = input("Introduce una cadena de texto:")
#cadena = "pwunoojdgioluhnaew"
cadena = cadena.lower()     # convertimos el texto a minúsculas para 
contador = 0                # reducir las condiciones a evaluar.
longitud = len(cadena)
vocales = "aeiou"
total_vocales = 0
while contador < longitud:
    
    if cadena [contador] in vocales:
        total_vocales += 1
        contador += 1
        
    else:
        contador += 1
        
print (total_vocales)


# 9.Crear un programa que nos diga si una cadena de texto, contiene las vocales “i” y “u”.
cadena = input('Introduce una cadena de texto en minúsculas: ')
for indice in range(len(cadena)):
	if cadena [indice] == "i" or cadena [indice] == "u":
		print ("La cadena contiene una i o una u")
  
cadena = input('Introduce una cadena de texto en minúsculas: ')
vocales = "iu"
for indice in range(len(cadena)):
    if cadena[indice] in vocales:
        print ("La cadena contiene una i o una u")


# 10. Desarrollar un programa que dado un número de mes (1 al 12), nos diga 
# el nombre del mes y liste los 11 siguientes meses.
# Pej, si introducimos un 8, el programa deberá decir Agosto, e imprimir en
# pantalla Agosto, Septiembre, Octubre, Noviembre, Diciembre, Enero, ... , Julio

mes = int(input("Introduce número de mes: "))
mes = mes - 1
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'\
,'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

a = mes
print ("El mes introducido es:", meses[mes])

for a in range (mes,12):
    print (meses[a])
    
for a in range (0,mes):
    print (meses[a])
