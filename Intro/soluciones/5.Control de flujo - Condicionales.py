#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 14:50:16 2022

@author: mydoctor
"""

# 1.Crea un programa que leyendo una lista ascendente de números del 1 al 5, 
# compruebe se la primera posición es mayor que la última.  Guardar dicha 
# lista en una variable llamada lista1. En caso de serlo, deberá mostrar en 
# pantalla ‘El primer elemento de la lista es mayor que el último’, en caso 
# contrario ‘El primer elemento de la lista es menor que el último’
lista1 = [1,2,3,4,5]

#lista1 = [2,5,3,1,4]
#lista1.sort()


if lista1 [0] > lista1 [4]:
    print ("El primer elemento de la lista es mayor que el último")
else:
    print ("El primer elemento de la lista es menor que el último")

    
# 2.Aprovechar el programa anterior y ordenar lista1 en sentido descendente. 
# Volver a ejecutar el código y comprobar que el resultado obtenido es el 
# opuesto al del punto1.

# Cambiamos el orden de la lista y ejecutamos el mismo código.
lista1.sort(reverse=True)

if lista1 [0] > lista1 [4]:
    print ("El primer elemento de la lista es mayor que el último")
else:
    print ("El primer elemento de la lista es menor que el último")

    
# 3.Crear un programa, que detecte si al introducir un número, éste es 
# positivo o negativo.  Deberás usar la función input para introducir el 
# número.  NOTA: input trabaja sólo con cadenas de texto, por lo que 
# deberás convertir el dato introducido a número.

numero = int(input("Escribe un número: "))
#numero = 10
if numero < 0:
    print("El número introducido es negativo")
else:
    print("El número introducido es positivo y es " + str(numero))

    
# 4. Crear un programa que sea capaz de ‘adivinar’ un número del 1 al 4 
# mediante el método de bisección.
#   1. Los pasos serían, elegir un número del 1 al 4.
#   2. El programa deberá preguntarnos si el número a adivinar es mayor que 2
#   3. Si la respuesta es positiva, deberá preguntarnos si el número es 3 o no 
#      y ya tendríamos el resultado para números elegidos superiores a 2.
#   Si la respuesta del punto 2 es negativa, tendremos que plantear el caso 
#   opuesto al del punto 3.

print("Piensa un número del 1 a 4.")
print("Contesta S (sí) o N (no) a las preguntas.")
primera = input("¿El número pensado es mayor que 2? ")

if (primera == "S" or primera == "s"):   # evaluamos su el valor introducido es S o s
    segunda = input("¿El número pensado es mayor que 3? ")
    if (segunda == "S" or segunda == "s"):
        print("El número pensado es 4.")
    else:
        print("El número pensado es 3")
else:
    segunda = input("¿El número pensado es mayor que 1? ")
    if (segunda == "S" or segunda == "s"):
        print("El número pensado es 2.")
    else:
        print("El número pensado es 1.")

# podemos reducir la complejidad del problema, reduciendo las posibilidades
# a la mitad.

primera = input("¿El número pensado es mayor que 2? ")
primera = primera.lower()

if primera == "s":   # evaluamos si el valor introducido s
    segunda = input("¿El número pensado es mayor que 3? ")
    segunda = segunda.lower()
    if segunda == "s":
        print("El número pensado es 4.")
    else:
        print("El número pensado es 3")
else:
    segunda = input("¿El número pensado es mayor que 1? ")
    segunda = segunda.lower()
    if segunda == "s":
        print("El número pensado es 2.")
    else:
        print("El número pensado es 1.")



# 5.Crear un programa que para una edad dada, compruebe las 3 condiciones
# siguientes:
#   1. Edad <0, muestre en pantalla ‘Edad negativa’.
#   2. 0 <= Edad <18, muestre en pantalla, ‘Menor de edad’.
#   3. Edad >= 18, muestre en pantalla, ‘Mayor de edad’.
#   Deberás plantear el ejercicio a través de if, elseif, else.


edad = int(input("¿Cuántos años tienes? "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad >= 0 and edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

    
# 6.Crear un programa que dado un número, nos diga si el número es 
# múltiplo de 2, de 4 y 2 o no es múltiplo de 2.  Tendrás que tener en cuenta
# que los múltiplos de 4 son múltiplos de 2, pero no al revés.  Por ello el 
# orden de las condiciones a evaluar, es relevante.

numero = int(input("Escribe un número: "))
if numero % 2 == 0:
    print(str(numero) + " es múltiplo de dos")
elif numero % 4 == 0:
    print(str(numero) + " es múltiplo de cuatro y de dos")
else:
    print(str(numero) + " no es múltiplo de dos")
    
# Vemos que en el caso previo, el programa no está evaluando correctamente
# los múltiplos de 4 ya que los múltiplos de 4 también lo son de 2.
# Cuando se evalua la primera condición, al cumplirse, se desechan el 
# resto.
    
# Deberíamos reescribir el código...
numero = int(input("Escribe un número: "))
if numero % 4 == 0:
    print(str(numero) + " es múltiplo de cuatro y de dos")
elif numero % 2 == 0:
    print(str(numero) + " es múltiplo de dos")
else:
    print(str(numero) + " no es múltiplo de dos")
    
    
# 7.Desarollar un programa que para 3 números dados, determine su orden 
# (de menor a mayor).  Introduce los 3 números, mediante sendas funciones 
# input (una función input para cada número a introducir)

x = int(input('Introduce el primero de los números a comparar: '))
y = int(input('Introduce el segundo de los números a comparar: '))
z = int(input('Introduce el último de los números a comparar: '))

if x > y and y > z:
    print("Orden:",x,y,z)
if x > z and z > y:
    print ("Orden:",x,z,y)
if z > x and x > y:
    print ("Orden:",z,x,y)
if z > y and y > x:
    print ("Orden:",z,y,x)
if y > x and x > z:
    print ("Orden:",y,x,z)
if y > z and z > x:
    print ("Orden:",y,z,x)
    
    
# 8.Desarrollar un programa que pida 2 palabras y nos diga si riman o no.  
# Si las 3 últimas letras son iguales, las palabras riman.  Si las 2 últimas 
# letras son iguales, las palabras riman poco.  Si solo 1 letra o ninguna son 
# iguales, las palabras no riman.  Ten en cuenta el tamaño mínimo de las 
# palabras a comparar, si no es de al menos 3 no podrás hacer las comparaciones.

palabra_uno = input ("Dime la primera palabra: ")
print ("")
palabra_dos = input ("Dime la segunda palabra: ")
print ("")

if len(palabra_uno) < 3 or len(palabra_dos) < 3:
    print ("Las palabras tienen menos de 3 letras")
    print ("")
elif palabra_uno[-3:] == palabra_dos[-3:]:
    print ("Riman")
    print ("")
elif palabra_uno[-2:] == palabra_dos[-2:]:
    print ("Riman un poco")
    print ("")
else:
    print ("No riman")
    print ("")