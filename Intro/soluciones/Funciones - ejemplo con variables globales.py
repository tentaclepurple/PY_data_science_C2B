# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 09:18:58 2022

@author: german
"""

def func_a():
    print ("Dentro de la función a")
def func_b(y):
    print ("Dentro de la función b")
    return y
def func_c(z):
    print ("Dentro de la función c")
    return z() # devuelve el valor de z que aquí es una función

print (func_a())
print (5 + func_b(2))
print (func_c(func_a))


# uso de variables globales
contador = 10

def reiniciar_contador():
	global contador
	contador = 0

def reiniciar_contador2():
	contador = 0



print(f'Contador antes es {contador}')
reiniciar_contador()
print(f'Contador después es {contador}')


reiniciar_contador2()
print(f'Contador después es {contador}')

# uso de variable local como variable global dentro del
# mismo contexto
def funcion_padre():
	valor = 10

	def funcion_anidada():
		nonlocal valor  # sólo funciona en python 3
		valor = 20
		print(f'Valor en función anidada es {valor}')

	print(f'Valor en función padre antes es {valor}')
	funcion_anidada()
	print(f'Valor en función padre después es {valor}')
    
funcion_padre()
