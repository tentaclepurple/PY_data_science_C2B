#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 1 10:19:57 2022

@author: mydoctor
"""
# 1. Crea una lista con los nombres de los 6 primeros días de la semana. Llama a esa
# lista, lista1
lista1 = ["Lunes","Martes","Miércoles","Jueves","Viernes",'Sábado']

# 2.Crea una lista con los números del 1 al 7, llama a esa lista, lista2
lista2 = list(range(1,8))
lista2 = [1,2,3,4,5,6,7]

type(range(1,8))

# 3. Crea las siguientes listas:
# lista3 = ["Lunes", 1, "Mayo", 2018]
# lista4 = [["Alberto", 1.75, 80],["Ana", 1.70, 65],["María", 1.90, 80]]
# lista5 = [["Stanley Kubrick", ["Senderos de Gloria", 1957]], ["Woody Allen", ["Hannah y sus hermanas", 1986]]]
lista3 = ["Lunes", 1, "Mayo", 2018]
lista4 = [["Alberto", 1.75, 80],["Ana", 1.70, 65],["María", 1.90, 80]]
lista5 = [["Stanley Kubrick", ["Senderos de Gloria", 1957]], ["Woody Allen", ["Hannah y sus hermanas", 1986]]]

# 4. De lista1, extrae:
# ▪ Segundo elemento,
# ▪ Primer elemento,
# ▪ Último elmento
lista1[1]
lista1[0]
lista1[-1]

# 5. Comprueba qué tipo de dato tenemos en el último elemento de lista1
type(lista1[-1])

# 6. De lista5, escribe el código para obtener los siguientes datos:
# ▪ Stanley Kubrick
# ▪ 1986
# ▪ ["Senderos de Gloria", 1957]
# ▪ ["Woody Allen", ["Hannah y sus hermanas", 1986]]
lista5[0][0]
lista5[1][1][1]
lista5[0][1]
lista5[1]

# 2 maneras de hacer lo mismo
lista5[1][1][1]
lista5[-1][-1][-1]

# 2 maneras de hacer lo mismo
lista5[0][1]
lista5[0][-1]

lista5[1]

# 7. Crea 2 copias de lista1, una en lista6 y otra en lista7. Después crea una nueva
# lista8 que sea un alias de lista7. Crea una lista vacía en lista9
lista6 = lista1[:]
lista7 = lista1[:]
lista8 = lista7
lista9 = []

# 8. Elimina el "Miércoles" de la lista6, así como el "Viernes" de la lista8.
# Comprueba la lista7.
lista6.remove ("Miércoles")
lista6
lista8.remove ("Viernes")
lista8
lista7

# 9. Ordena la lista1, lista2 y lista3. Estudia los resultados obtenidos.
lista1.sort()
lista1
lista2.sort()
lista2
lista3.sort()
lista3

# 10.Comprueba si ‘lunes’ existe en lista3.
'lunes' in lista3

# 11.Modifica el tercer elemento de la lista2, 
# para que incluya el número 1000
lista2[2] = 1000

# 12.Añade ‘Domingo’ a la lista1.
lista1.append("Domingo")
lista1

# 13.Ejecuta el comando necesario para obtener el tamaño de la lista5. ¿Cuál es el
# tamaño de la segunda lista en la lista4?
len(lista5)
len(lista4[1])

# 14.Extiende la lista6 con la lista3.
lista6.extend(lista3)
lista6
# Otra manera
lista6 = lista6 + lista3

# 15.Inserta un elemento al inicio de la lista6
lista6.insert(0, "prueba")

# 16.Inserta un elemento en la posición 3 del índice de la lista6
lista6.insert(3, "inserción")

# 17.Insertar un elemento en la primera posición de la primera lista de lista4
lista4[0].insert(0,"inserción")


###### Comprobación de si una lista es un alias o un copia
lista_cpy=lista1.copy()
lista_alias=lista1
print(lista1.__contains__ == lista_cpy.__contains__)
print(lista1.__contains__ == lista_alias.__contains__)










