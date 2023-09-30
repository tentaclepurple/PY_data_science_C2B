#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 11:21:30 2022

@author: mydoctor
"""

#1. Crea un diccionario que contenga las siguientes claves y valores:
#  ◦ Claves: 1, 2, 3, 4, 5
#  ◦ Valores: 1, 4, 9, 16, 25
#  Guarda el resultado en diccionario1
diccionario1 = {1:1, 2:4, 3:9, 4:16, 5:25}

# 2.Una vez creado el diccionario, extraer sus valores.
diccionario1.values()

# 3.Extrae el valor de la clave 2
diccionario1.get(2)
diccionario1 [2]

# 4.Añade un nuevo elemento (clave y valor).  Clave 6 y valor 35.  Comprueba el resultado.
diccionario1 [6] = 35
diccionario1.values()
diccionario1.keys()

#a = list(diccionario1.values())
# 5.Modifica el valor recién creado por el de 36
diccionario1 [6] = 36

# 6.Elimina la clave 5
diccionario1.pop(5)
diccionario1.values()
diccionario1.keys()

# 7.Añadir un nuevo elemento (clave y valor), donde la clave sea 7 y el valor una lista compuesta de los valores ‘A’, ‘B’ y ‘C’
diccionario1 [7] = ['A','B','C']

# 8.Extraer el segundo valor de la lista correspondiente a la última clave ('B')
diccionario1[7][-2]


# Caso planteado en clase, donde se definen como texto las claves
diccionario2 = {"1":1, "2":4, "3":9, "4":16, "5":25}
diccionario2 ["6"] = "36"
diccionario2 ["7"] = ['A','B','C']
diccionario2["7"][-1]
# Este caso, al ser el valor de la clave "6" de tipo texto,
# es iterable y por tanto podemos extraer el valor de su posición
# en el índice
diccionario2["6"][-2]
diccionario2["6"][-1]

# Un poco más complicado.  Añadir a una nueva clave una lista.  
# Después extraer de dicha clave la segunda posición (elemento), del primer
# elemento de la lista
diccionario2 ["8"] = ['ADE','B','C']
diccionario2 ["8"][0][1] # extracción de D dentro de la lista existente en 
                         # la clave "8"


# Otro caso más complicado mediante el uso de alias
# Modificamos la clave 8 del diccionario anterior
diccionario2 ["8"][0] = "abcde"

# Creamos una lista y alias a dicha lista (lista1)
lista= [0,1,2]
lista1 = lista

# Añadimos una nueva clave (lista_alias) al diccionario anterior que contenga
# la lista creada anteriormente
diccionario2 ["lista_alias"] = lista

# Añadimos algo a la lista1 (el alias) y vemos que el diccionario
# recoge el cambio
lista1.append(3)
diccionario2

# Comprobamos cómo el valor de la clave '8' se actualiza
# en consecuencia.

# En este caso, vemos como lista2 se actualiza con cualquier cambio en 
# diccionario2, y a su vez cualquier cambio en lista2 influye en diccionario2
# y lista1
lista2 = diccionario2 ["lista_alias"]
lista2.append(444)
lista1.append(555)
diccionario2
lista2
lista1
